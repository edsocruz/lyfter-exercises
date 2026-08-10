import psycopg2
import random

from faker import Faker

fake = Faker()

def seed_database():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432
        )

        cursor = connection.cursor()

        user_ids = []
        car_ids = []

    #crear los 200 usuarios
        for i in range(200):
            full_name = fake.name()
            email = fake.unique.email()
            username = fake.unique.user_name()
            password = fake.password()
            birth_date = fake.date_of_birth(minimum_age=18,maximum_age=80)

            account_status = random.choice(["active","inactive","arrears"])
            cursor.execute(
                """
                INSERT INTO lyfter_car_rental.Users
                (name, email, username, password, birth_date, account_status)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, name, email, username, password, birth_date, account_status;
                """,(full_name,email,username,password,birth_date,account_status)
            )
            
            user_id = cursor.fetchone()[0]
            user_ids.append(user_id)

        print("Usuarios de prueba creados")

    #Crear los carros 
        brands = [
            "Toyota",
            "Honda",
            "Ford",
            "Chevrolet",
            "Hyundai",
            "Nissan",
            "Mazda"
        ]

        models = [
            "Corolla",
            "Civic",
            "Focus",
            "Sentra",
            "Elantra",
            "Mazda 3",
            "Explorer"
        ]

        for i in range(100):
            brand = random.choice(brands)
            model = random.choice(models)
            production_year = random.randint(2005, 2026)
            status = random.choice(["available","maintenance","unavailable"])

            cursor.execute(
                """
                INSERT INTO lyfter_car_rental.Cars
                (brand, model, production_year, status)
                VALUES (%s, %s, %s, %s)
                RETURNING id, brand, model, production_year, status;
                """,(brand,model,production_year,status)
            )
            

            car_id = cursor.fetchone()[0]
            car_ids.append(car_id)

        print("Carros de prueba creados")

        #Crear las rentas

        rent_quantity = random.randint(50, 150)
        for i in range(rent_quantity):
            id_user = random.choice(user_ids)
            id_car = random.choice(car_ids)
            #acá hay que pasarle la fecha de inicio y fin, en el star_date el -2y quiere decir que las fechas 
            # se generan 2 años en el pasado con respecto a la fehca actual, y el +30d, quiere decir dentro 
            # de 30 dias en el futuro a la fecha actual 
            return_date = fake.date_between(
                start_date="-2y",
                end_date="+30d"
            )

            rental_status = random.choice(["active","completed"])

            cursor.execute(
                """
                INSERT INTO lyfter_car_rental.Users_Cars
                (id_user, id_car, return_date, rental_status)
                VALUES (%s, %s, %s, %s) returning id, id_user, id_car, return_date, rental_status;
                """,
                (id_user,id_car,return_date,rental_status)
            )
            

        connection.commit()

        print(f"{rent_quantity} rentas creadas")
        print("Generación de datos completa")

    except Exception as error:
        if connection:
            connection.rollback()
        print("Error creating seed:", error)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
seed_database()