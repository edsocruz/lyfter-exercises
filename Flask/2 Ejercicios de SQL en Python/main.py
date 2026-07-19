from Repositories.usersRepository import UserRepository
from Repositories.carsRepository import CarsRepository
from Repositories.usersCarsRepository import RentRepository
from flask import Flask, request
from db_settings import PgManager

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)

userRepository = UserRepository(db_manager)
carsRepository =  CarsRepository(db_manager)
rentRepository = RentRepository(db_manager)


#Creación

#Crear un usuario nuevo
@app.route("/users", methods=["POST"])
def create_user():
    #como estos campos son obligatorios validamos que vengan en el request
    required_fields = ["full_name","email","username","password","birth_date","account_status"]

    for field in required_fields:
        value = request.json.get(field)

        if value is None or (isinstance(value, str) and value.strip() == ""):
            return {"message": f"El campo '{field}' es obligatorio."}, 400

    full_name = request.json.get("full_name")
    email = request.json.get("email")
    username = request.json.get("username")
    password = request.json.get("password")
    birth_date = request.json.get("birth_date")
    account_status = request.json.get("account_status")
    if (not account_status == "active") and (not account_status == 'inactive') and (not account_status == 'arrears'): return {"error": "status debe ser 'active' o 'inactive' o 'arrears'"}, 400

    data_created = userRepository.create(full_name,email,username,password,birth_date,account_status)

    return {"element added": data_created}, 201


#Crear un automóvil nuevo
@app.route("/cars", methods = ["POST"])
def create_car():
    required_fields = ["status","brand","model","production_year"]

    for field in required_fields:
        value = request.json.get(field)
        if value is None or (isinstance(value, str) and value.strip() == ""):
            return {"message": f"El campo '{field}' es obligatorio."}, 400
        
    status = request.json.get("status")
    if (not status == "rented") and (not status == 'available') and (not status == 'maintenance') and (not status == 'unavailable'): return {"error": "status_filter debe ser 'rented' o 'available' o 'maintenance' o 'unavailable'"}, 400
    brand = request.json.get("brand")
    model = request.json.get("model")
    production_year = request.json.get("production_year")

    data_created = carsRepository.create(brand, model, production_year, status)
    return {"element added": data_created}, 201



#Crear un alquiler nuevo
@app.route("/rents", methods = ["POST"])
def create_rent():
    required_fields = ["id_user", "id_car", "return_date"]
    for field in required_fields:
        value = request.json.get(field)
        if value is None or (isinstance(value, str) and value.strip() == ""):
            return {"message": f"El campo '{field}' es obligatorio."}, 400
        
    user = userRepository.get_by_id(request.json.get("id_user"))
    if not user:
        return {"Message":f'El usuario con el id {request.json.get("id_user")} no existe'}, 404
    car = carsRepository.get_by_id(request.json.get("id_car"))
    if not car:
        return {"Message":f'El carro con el id {request.json.get("id_car")} no existe'}, 404

    id_user = request.json.get("id_user")
    id_car = request.json.get("id_car")
    return_date = request.json.get("return_date")
    #rental_status = request.json.get("rental_status") este valor no lo ocupamos ya que siempre que renten un carro, el valor del estatus será active, el valor solo se cambia cuando devuelven el carro y el estatus pasa a ser completed

    #Ok ya valido que el user y el carro existan, ahora debo validar que el usuario esta activo y el carro disponible
    if not user.get("account_status") == "active":
        return {"Message":f'El usuario no se encuetra activo o esta mororso'}, 401
    if not car.get("status") == "available":
        return {"Message":f'El carro no se encuetra disponible para su alquiler'}, 401
    #Si el usuario  y el carro existen y estan disponibles, entonces creamos el registro de la renta
    rent_created = rentRepository.create(id_user, id_car, return_date, "active") #el valor del status va quemado ya que siempre que se crea una renta el estado inicial es active
    #tengo que cambiar el estado del carro 
    car_updated = carsRepository.update(id_car, car["brand"], car["model"], car["production_year"], "rented") 
    return {"Rent created": rent_created,
        "Car updated": car_updated}, 200



#Modificación

#Cambiar el estado de un automovil
@app.route("/cars/<id_car>", methods = ["PATCH"])
def update_car(id_car):
    #Si en el request viene algo entonces lo tomamos y se lo asignamos
    #Recordatorio: usar el .get() a la hora de acceder el valor de un diccionario, ya que si no lo hacemos podria dar error si simplemente tratamos de acceder con request.json["valor"] en vez de hacer request.json.get("valor")
    car = carsRepository.get_by_id(id_car)
    if not car:
        return {"Message":f'El carro con el id {id_car} no existe'}, 404
    if not (request.json.get("status") == None): #si en status viene algo, vamos a validar que sea un valor esperado
        status = request.json.get("status")
        if (not status == "rented") and (not status == 'available') and (not status == 'maintenance') and (not status == 'unavailable'):
            return {"Error": "status_filter debe ser 'rented' o 'available' o 'maintenance' o 'unavailable'"}, 400
        else:
            car["status"] = status
    
    if (request.json.get("brand")):
        car["brand"] = request.json.get("brand")
    
    if (request.json.get("model")):
        car["model"] = request.json.get("model")

    if(request.json.get("production_year")):
        car["production_year"] = request.json.get("production_year")
    
    car_updated = carsRepository.update(id_car, car["brand"], car["model"], car["production_year"], car["status"])

    return {"Car updated": car_updated}, 200


#Cambiar el estado de un usuario
@app.route("/users/<id_user>", methods=["PATCH"])
def update_user(id_user):

    user = userRepository.get_by_id(id_user) #Recordemos que esto nos da un diccionario 

    if not user:
        return {
            "message": f"El usuario con el id {id_user} no existe"
        }, 404

    # Si vienen nuevos valores, los usamos; si no, conservamos los actuales
    allowed_fields = ["full_name","email","username","password","birth_date"]

    for field in allowed_fields:
        value = request.json.get(field)
        if value is not None:
            user[field] = value

    # Validacion especial para account_status
    if request.json.get("account_status") is not None:
        account_status = request.json.get("account_status")
        if account_status not in ["inactive", "active", "arrears"]:
            return {
                "error": "account_status debe ser 'inactive', 'active' o 'arrears'"
            }, 400

        user["account_status"] = account_status

    updated_user = userRepository.update(
        id_user,
        user["full_name"],
        user["email"],
        user["username"],
        user["password"],
        user["birth_date"],
        user["account_status"]
    )

    return {"User updated": updated_user}, 200


#Completar un alquiler
@app.route("/rents/<id_rent>/complete", methods=["PATCH"])
def update_rent_complete(id_rent):
    rent = rentRepository.get_by_id(id_rent) #Recordemos que esto nos da un diccionario 
    if not rent: return {"message": f"La renta con el id {id_rent} no existe"}, 404
    #Se marca la renta como completada
    updated_rent = rentRepository.update(id_rent, rent["id_user"], rent["id_car"], rent["return_date"], "completed")
    #Se libera el carro: pasa de rented a maintenance
    car = carsRepository.get_by_id(rent["id_car"])
    car_updated = carsRepository.update(rent["id_car"], car["brand"], car["model"], car["production_year"], "maintenance")
    return {"Rent completed": updated_rent}, 200


#Cambiar el estado de un alquiler
@app.route("/rents/<id_rent>", methods=["PATCH"])
def update_rent_status(id_rent):
    rent = rentRepository.get_by_id(id_rent) #Recordemos que esto nos da un diccionario 

    if not rent: return {"message": f"El usuario con el id {id_rent} no existe"}, 404

    # Si vienen nuevos valores, los usamos; si no, conservamos los actuales
    allowed_fields = ["rental_status"]

    for field in allowed_fields:
        value = request.json.get(field)
        if value is not None:
            rent[field] = value

    # Validacion especial para rental_status
    if request.json.get("rental_status") is not None:
        rental_status = request.json.get("rental_status")
        if rental_status not in ["active", "completed"]:
            return {
                "error": "rental_status debe ser 'completed' o 'active' "
            }, 400

        rent["rental_status"] = rental_status

    updated_rent = rentRepository.update(
        id_rent,
        rent["id_user"],
        rent["id_car"],
        rent["return_date"],
        rent["rental_status"]
    )

    return {"Rent updated": updated_rent}, 200

#Flagear un usuario como moroso
@app.route("/users/<id_user>/arrears", methods=["PATCH"])
def update_user_arrears(id_user):
    user = userRepository.get_by_id(id_user) #Recordemos que esto nos da un diccionario 
    if not user: return {"message": f"El usuario con el id {id_user} no existe"}, 404
    updated_user = userRepository.update(id_user, user["full_name"], user["email"], user["username"], user["password"], user["birth_date"], "arrears")
    return {"User updated": updated_user}, 200


#Listado

#Listar todos los usuarios
@app.route("/users", methods=["GET"])
def show_users():
    filtered_users = []
    # cargamos la lista a una variable
    filtered_users = userRepository.get_all()

    if (request.args.get("id")): # si el valor existe entonces hacemos el filtrado
        id_filter = request.args.get("id")
        filtered_users = list(
            filter(lambda item: item["id"] == int(id_filter), filtered_users))
    
    if (request.args.get("full_name")): #En caso de tener mas de 1 filtro activo, el filtrado lo haremos sobre la lista resultante despues de cada filtro
        full_name_filter = request.args.get("full_name")  
        filtered_users = list(
            filter(lambda item: item["full_name"] == full_name_filter, filtered_users))
    
    if (request.args.get("email")):  
        email_filter = request.args.get("email")
        filtered_users = list(
            filter(lambda item: item["email"] == email_filter, filtered_users))
    
    if (request.args.get("username")):
        username_filter = request.args.get("username")  
        filtered_users = list(
            filter(lambda item: item["username"] == username_filter, filtered_users))
    
    if (request.args.get("password")):
        password_filter = request.args.get("password")  
        filtered_users = list(
            filter(lambda item: item["password"] == password_filter, filtered_users))
    
    if (request.args.get("birth_date")):
        birth_date_filter = request.args.get("birth_date")  
        filtered_users = list(
            filter(lambda item: item["birth_date"] == birth_date_filter, filtered_users))
    
    if (request.args.get("account_status")):
        status = request.args.get("account_status")
        if (not status == 'active') and (not status == 'inactive') and (not status == 'arrears'):
            return {"error": "account_status debe ser 'active', 'inactive' o 'arrears'"}, 400
        filtered_users = list(
            filter(
                lambda item: item["account_status"] == status,filtered_users
                )
            )
    #Si los parametros existen entonces la lista se va a ir reduciendo, dejando unicamente los resultados que cumplan los filtros
    return filtered_users
    

#Listar todos los automóviles
@app.route("/cars", methods=["GET"])
def show_cars():
    filtered_cars = []
    # cargamos la lista a una variable
    filtered_cars = carsRepository.get_all()

    if (request.args.get("id")): # si el valor existe entonces hacemos el filtrado
        id_filter = request.args.get("id")
        filtered_cars = list(
            filter(lambda item: item["id"] == int(id_filter), filtered_cars))
    
    if (request.args.get("brand")): 
        brand_filter = request.args.get("brand")  
        filtered_cars = list(
            filter(lambda item: item["brand"] == brand_filter, filtered_cars))
    
    if (request.args.get("model")):  
        model_filter = request.args.get("model")
        filtered_cars = list(
            filter(lambda item: item["model"] == model_filter, filtered_cars))
    
    if (request.args.get("production_year")):
        production_year_filter = request.args.get("production_year")  
        filtered_cars = list(
            filter(lambda item: item["production_year"] == production_year_filter, filtered_cars))

    if (request.args.get("status")):
        status_filter = request.args.get("status").strip().lower()
        if (not status_filter == "rented") and (not status_filter == 'available') and (not status_filter == 'maintenance') and (not status_filter == 'unavailable'):
            return {"error": "status_filter debe ser 'rented' o 'available' o 'maintenance' o 'unavailable'"}, 400
        else:
            filtered_cars = list(
                filter(lambda item: item["status"] == status_filter,filtered_cars))
        
    return filtered_cars
    

#Listar todos los alquileres
@app.route("/rents", methods=["GET"])
def show_rents():
    filtered_rents = []
    # cargamos la lista a una variable
    filtered_rents = rentRepository.get_all()

    if (request.args.get("id")): # si el valor existe entonces hacemos el filtrado
        id_filter = request.args.get("id")
        filtered_rents = list(
            filter(lambda item: item["id"] == int(id_filter), filtered_rents))
    
    if (request.args.get("id_user")): 
        id_user_filter = request.args.get("id_user")  
        filtered_rents = list(
            filter(lambda item: item["id_user"] == id_user_filter, filtered_rents))
    
    if (request.args.get("id_car")):  
        model_filter = request.args.get("id_car")
        filtered_rents = list(
            filter(lambda item: item["id_car"] == model_filter, filtered_rents))
    
    if (request.args.get("return_date")):
        production_year_filter = request.args.get("return_date")  
        filtered_rents = list(
            filter(lambda item: item["return_date"] == production_year_filter, filtered_rents))

    if (request.args.get("rental_status")):
        rental_status_filter = request.args.get("rental_status")
        if (not rental_status_filter == "active") and (not rental_status_filter == 'completed'):
            return {"error": "rental_status_filter debe ser 'active' o 'completed'"}, 400
        else: 
            filtered_rents = list(
                filter(lambda item: item["rental_status"] == rental_status_filter,filtered_rents))
        
    return filtered_rents






if __name__ == "__main__":
    try:
        app.run(host="localhost", port=8080, debug=True)
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
