from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from Model.base import Base
from Model.users import User
from Model.addresses import Address
from Model.cars import Car

DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DB_URI, echo=False)

Base.metadata.create_all(engine)

fake = Faker()

brands = ["Toyota", "Honda", "BMW", "Nissan", "Mazda"]
models = ["Sedan", "SUV", "Pickup", "Coupe"]

with Session(engine) as session:

    # Generar 20 usuarios
    for i in range(20):

        user = User(
            name=fake.name()[:30], #acá se delimita la cantidad maxima de caracteres 
            email=fake.email()[:30]
        )
        session.add(user)

        # Generar entre 1 y 3 direcciones por usuario
        for j in range(fake.random_int(min=1, max=3)):
            address = Address(
                address=fake.street_address()[:30],
                user=user
            )
            session.add(address)

        # Generar entre 0 y 3 carros por usuario
        for j in range(fake.random_int(min=0, max=3)):

            car = Car(
                plate=fake.bothify(text="???-###").upper(), #Para genrerar la placa de los carros
                brand=fake.random_element(elements=brands),
                model=fake.random_element(elements=models),
                year=fake.random_int(min=2000, max=2026),
                owner=user
            )
            session.add(car)

    # Generar 5 carros sin propietario
    for i in range(5):

        car = Car(
            plate=fake.bothify(text="???-###").upper(),
            brand=fake.random_element(elements=brands),
            model=fake.random_element(elements=models),
            year=fake.random_int(min=2000, max=2026),
            owner=None
        )

        session.add(car)

    session.commit()

    print("Seed completed successfully!")