import sqlalchemy

from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, Column, Integer, String, text, ForeignKey, create_engine 
print(sqlalchemy.__version__)

#las contraseñas y nombres de usuario se deben pasar los caracteres especiales URL encoded, en terminos sencillos
# se puede usar esta liberia para pasarle la contraseña y que él la codifique 
#import urllib.parse
#print(urllib.parse.quote_plus("kx@jj5/g"))


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

#Método manual 
try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()  # Cerramos la conexion cuando terminamos
except Exception as e:
    print("Connection failed:", e)

#Método recomendado para hacer un select, solo con el connect
# SELECT
#with engine.connect() as connection:
#    ...
#Método recomendado para hacer una modificacion en la base de datos
# INSERT / UPDATE / DELETE
#with engine.begin() as connection:
#    ...

#-----------------------------------------------------------------------------PARTE 2
# Plantee una DB con tablas para usuarios, direcciones y automóviles.

#Automoviles
# - ID
# - Matricula
# - Marca
# - Modelo
# - Año
# - Propietario (FK)

#Direcciones 
# - ID
# - Direccion
# - Usuario (FK)

#Usuarios 
# - ID
# - Nombre
# - Correo


metadata_obj = MetaData()

users_table = Table(
    "users", metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("email", String(30), nullable=False),
)

#Column("",),

addresses_table = Table(
    "addresses", metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("address", String(40), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False)
)

cars_table = Table(
    "cars", metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("plate", String(6), nullable=False),
    Column("brand", String(10), nullable=False),
    Column("model", String(10), nullable=False),
    Column("year", Integer, nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=True)
)

#-----------------------------------------------------------------------------PARTE 3
#Realice un script que valide si las tablas existen, y si no las cree en el momento de su ejecución.
metadata_obj.create_all(engine)


#-----------------------------------------------------------------------------PARTE 4

from Repositories.userRepository import UserRepository
from Repositories.addressRepository import AddressRepository
from Repositories.carRepository import CarRepository


with Session(engine) as session:
    user_repository = UserRepository(session) # EL repository siempre recibe la sesion

    # Create a user
    user_repository.create("Samantha", "samantha@gmail.com")
    
    # Select users
    users = user_repository.select()
    for user in users:
        print(user.id, user.name, user.email)

    #Update a user
    user_repository.update(5,'Sara Patricia', "sardimar@gmail.com")

    #Delete a user 
    user_repository.delete(1)


    address_repository = AddressRepository(session)
    # Create an address
    user_obj = user_repository.get(4)
    address_repository.create('Heredia',user_obj)
    
    # Select addresses
    addresses = address_repository.select()
    for address in addresses:
        print(address.id, address.address, address.user_id)
    
    #Delete an address
    address_repository.delete(6)
    
    #Update an address
    updated_address = address_repository.update(4,"San José", 7)
    print([updated_address.id, updated_address.address, updated_address.user_id])

    car_repository = CarRepository(session)
    #Create a Car
    user_obj = user_repository.get(4)
    created_car = car_repository.create('ABC123', 'Toyota', 'Hilux', 2020)
    print([created_car.id, created_car.plate, created_car.brand, created_car.model, created_car.year, created_car.user_id])
    
    #Select cars
    cars = car_repository.select()
    for item in cars:
        print(item.id, item.plate, item.brand, item.model, item.year, item.user_id)
    
    #Update Car
    updated_car = car_repository.update(1,'XYZ098', 'BYD', 'Seagull', 2025,4)
    print([updated_car.id, updated_car.plate, updated_car.brand, updated_car.model, updated_car.year, updated_car.user_id])

    #Link Car-user
    updated_car = car_repository.link_a_user(4, 7)
    print([updated_car.id, updated_car.plate, updated_car.brand, updated_car.model, updated_car.year, updated_car.user_id])

    #Delete Car
    car_repository.delete(5)