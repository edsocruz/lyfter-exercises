import psycopg2
import csv
from pathlib import Path # Esta libreria nos ayuda a no tener problemas con los / y \ en windows y mac
from datetime import datetime


def create_backup():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(dbname="postgres",user="postgres",password="postgres",host="localhost",port=5432)
        cursor = connection.cursor()

        #acá creamos esta carpeta tomando como referencia este file, que se cree en esta misma direccion
        backup_folder = Path(__file__).parent / "db_backups"
        backup_folder.mkdir(exist_ok=True)
        #os.makedirs("db_backups", exist_ok=True)

        current_date = datetime.now().strftime("%Y-%m-%d")

        tables = {
            "users": "lyfter_car_rental.Users",
            "cars": "lyfter_car_rental.Cars",
            "rents": "lyfter_car_rental.Users_Cars"
        }

        for file_name, table_name in tables.items():
            cursor.execute(f"select * from {table_name}")
            rows = cursor.fetchall()
            # cursor.description contiene los nombres de las columnas
            column_names = [column[0] for column in cursor.description]

            #file_path = f"db_backups/backup_{file_name}_{current_date}.csv"
            file_path = backup_folder / f"backup_{file_name}_{current_date}.csv"
            
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                #headers
                writer.writerow(column_names)
                #info
                writer.writerows(rows)
            print(f"Backup created: {file_path}")

    except Exception as error:
        print("Error creating backup:", error)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
create_backup()