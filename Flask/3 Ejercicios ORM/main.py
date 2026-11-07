import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine 
print(sqlalchemy.__version__)

#las contraseñas y nombres de usuario se deben pasar los caracteres especiales URL encoded, en terminos sencillos
# se puede usar esta liberia para pasarle la contraseña y que él la codifique 
#import urllib.parse
#print(urllib.parse.quote_plus("kx@jj5/g"))


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=False)#En true se muestran los comandos SQL que se ejecutan detras de camaras

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

from Model.base import Base
from Model.users import User
from Model.cars import Car
from Model.addresses import Address
#Se importan todas las clases que se van a crear en el metadata

Base.metadata.create_all(engine)
print(Base.metadata.tables.keys())


#-----------------------------------------------------------------------------PARTE 3
#Realice un script que valide si las tablas existen, y si no las cree en el momento de su ejecución.
#metadata_obj.create_all(engine)


#-----------------------------------------------------------------------------PARTE 4

from Repositories.userRepository import UserRepository
from Repositories.addressRepository import AddressRepository
from Repositories.carRepository import CarRepository


with Session(engine) as session:

    print("----------------------------------Users")

    user_repository = UserRepository(session) # EL repository siempre recibe la sesion

    # Create a user
    user_repository.create("Samantha", "samantha@gmail.com")
    user_repository.create("Sara", "sara@gmail.com")
    user_repository.create("Edso", "edso@gmail.com")
    user_repository.create("Edgar", "Edgar@gmail.com")
    user_repository.create("Sonia", "sonia@gmail.com")
    user_repository.create("Milda", "milda@gmail.com")
    user_repository.create("Fabio", "fabio@gmail.com")
    user_repository.create("Juanito", "juanitomoraporras@gmail.com")
    
    # Select users
    users = user_repository.select()
    for user in users:
        print(user.id, user.name, user.email)

    #Update a user
    user_updated = user_repository.update(2,'Sara Patricia', "sardimar@gmail.com")
    print(user_updated.id, user_updated.name ,user_updated.email)

    #Delete a user 
    deleted_user = user_repository.delete(8)
    print(deleted_user.id, deleted_user.name ,deleted_user.email)



    print("----------------------------------Addresses")
    address_repository = AddressRepository(session)
    # Create an address
    address_repository.create('Heredia',user_repository.get(1))
    address_repository.create('Barva',user_repository.get(2))
    address_repository.create('Santo Domingo',user_repository.get(3))
    address_repository.create('Santa Bárbara',user_repository.get(4))
    address_repository.create('San Rafael',user_repository.get(5))
    address_repository.create('San Isidro',user_repository.get(6))
    address_repository.create('Belén',user_repository.get(7))
    address_repository.create('Flores',user_repository.get(7))
    
    # Select addresses
    addresses = address_repository.select()
    for address in addresses:
        print([address.id, address.address, address.user_id, address.user.name])
    
    #Delete an address
    address_repository.delete(8)
    
    #Update an address
    updated_address = address_repository.update(7,"San Pablo", user_repository.get(6))
    print([updated_address.id, updated_address.address, updated_address.user_id, updated_address.user.name])


    print("-------------------------------------------------------------------tengo que corregir estos de carros")
    car_repository = CarRepository(session)
    #Create a Car
    user_obj = user_repository.get(4)
    created_car = car_repository.create('DOD330', 'Dodge', 'Durango', 2027)
    created_car = car_repository.create('DOD331', 'Dodge', 'Challenger', 2026)
    created_car = car_repository.create('DOD332', 'Dodge', 'Charger', 2025)
    created_car = car_repository.create('DOD430', 'Jeep', 'Wrangler', 2027)
    created_car = car_repository.create('DOD431', 'Jeep', 'Wagoneer S', 2026)
    created_car = car_repository.create('DOD432', 'Jeep', 'Cherokee', 2025)


    #Select cars
    cars = car_repository.select()
    print("----------------------------------Cars")
    for item in cars:
        print(item.id, item.plate, item.brand, item.model, item.year)
    
    #Update Car
    updated_car = car_repository.update(1,'XYZ098', 'BYD', 'Seagull', 2025, user_obj)
    print([updated_car.id, updated_car.plate, updated_car.brand, updated_car.model, updated_car.year, updated_car.owner.id, updated_car.owner.name])


    #Link Car-user
    updated_car = car_repository.link_user(6, user_obj)
    print([updated_car.id, updated_car.plate, updated_car.brand, updated_car.model, updated_car.year, updated_car.owner.id, updated_car.owner.name])

    #Delete Car
    car_repository.delete(5)

    
    print("----------------------------------")
    print("Nombre de usuario: ",user_obj.name)
    print("Carros: ")
    for car in user_obj.cars:
        print(car.brand, car.model, car.year)
    print("----------------------------------")
    print("Direcciones")
    for address in user_obj.addresses:
        print(address.address)
