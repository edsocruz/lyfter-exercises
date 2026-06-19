from flask import Flask, request, jsonify
import json


app = Flask(__name__)


# All data must be saved on a JSON file
def read_json_file(path=''):  # acá paso de un Json a un diccionario de Python
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


# acá paso de un diccionario de Python a un Json
def write_json_file(path, information):
    with open(path, 'w') as json_file:
        json.dump(information, json_file)

#Custom Exceptions
class BadRequestError(Exception):
    pass

class NotFoundError(Exception):
    pass

# Each task
# ID
# Title
# Description
# State

@app.route("/")
def root():
    return "<h1>Task Homework</h1>"

# Read task
@app.route("/tasks", methods=["GET"])
def show_tasks():
    filtered_task = []
    # cargamos la lista a una variable
    filtered_task = read_json_file("tasks.json")
    # accedemos al valor del query parameter
    task_filter = request.args.get("state")
    if task_filter:  # si el valor existe entonces hacemos el filtrado
        filtered_task = list(
            filter(lambda item: item["state"] == task_filter, filtered_task))
        return {"data": filtered_task}
    else:
        # Si el query parameter no existe entonces devolvemos toda la lista inicial
        return {"data": filtered_task}


def validate_id():
    if "id" not in request.json:
        raise ValueError("ID missing from the body")
    elif not request.json["id"]:
        raise ValueError("ID can not be empty")

def validate_title():
    if "title" not in request.json:
        raise ValueError("Title missing from the body")
    elif not request.json["title"]:
        raise ValueError("Title can not be empty")
    
def validate_description():
    if "description" not in request.json:
        raise ValueError("Description missing from the body")
    elif not request.json["description"]:
        raise ValueError("Description can not be empty")
    
def validate_state():
    if "state" not in request.json:
        raise ValueError("State missing from the body")
    elif not request.json["state"]:
        raise ValueError("State can not be empty")
    
def validate_state_values():
    if (request.json["state"] != "Completada") and (request.json["state"] != "Por hacer") and (request.json["state"] != "En progreso"):
        raise BadRequestError("The only valid states for status are: 'Completada', 'Por hacer', 'En progreso'")
        

# Create task
@app.route("/tasks", methods=["POST"])
def add_task():
    try:
        id_already_created = False
        task_list = []
        task_list = read_json_file("tasks.json")

        #Primero se valida que estos campos existan, ya luego se accede a los valores para validarlos
        validate_id()
        validate_title()
        validate_description()
        validate_state()
        validate_state_values()
        
        for item in task_list:
            if item["id"] == request.json["id"]:
                id_already_created = True
                break
        
        if id_already_created:
            raise ValueError("This ID is already used, choose a different one")
        
        task_list.append(
            {
                "id": request.json["id"],
                "title": request.json["title"],
                "description": request.json["description"],
                "state": request.json["state"]
            }
        )
        write_json_file('tasks.json', task_list)

        #Acá se podría mostrar el ultimo elemento de la lista pero prefiero buscar nuevamente el 
        # elmento que coincida con el ID que se acaba de crear, y no depender del orden de la 
        # lista sino de los datos
        for item in task_list: 
            if item["id"] == request.json["id"]:
                task_found = item
                return {"element added": task_found}, 201

        
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except BadRequestError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500

# Update task
@app.route("/tasks/<task_id>", methods=["PATCH"])
def update_task(task_id):
    try:
        id_already_created = False

        tasks_list = []
        tasks_list = read_json_file("tasks.json")  # cargamos el archivo
        task_found = None

        for item in tasks_list: #validamos que el ID exista
            if item["id"] == task_id:
                id_already_created = True
                task_found = item
                break

        if not id_already_created:
                raise NotFoundError(f"ID: {task_id} does not exist")
        else:
            body = request.json

            if "id" in body:
                task_found["id"] = body["id"]
            if "title" in body:
                task_found["title"] = body["title"]
            if "description" in body:
                task_found["description"] = body["description"]
            if "state" in body:
                validate_state_values()
                task_found["state"] = body["state"]

            write_json_file('tasks.json', tasks_list)

            return task_found
    
    except NotFoundError as ex:
        return jsonify(message=str(ex)), 404
    except BadRequestError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500
        

# Delete task
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        tasks_list = []
        tasks_list = read_json_file("tasks.json")  # cargamos el archivo
        id_already_created = False

        for item in tasks_list: #validamos que el ID exista
            if item["id"] == task_id:
                id_already_created = True
                break

        if not id_already_created:
                raise NotFoundError(f"ID: {task_id} does not exist")
        else:
            for index,item in enumerate(tasks_list):
                if item["id"] == task_id:
                    tasks_list.pop(index)
                    break

        write_json_file('tasks.json', tasks_list)

        return jsonify(), 204
    
    except NotFoundError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500


if __name__ == "__main__":
    try:
        app.run(host="localhost", port=8080, debug=True)
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
