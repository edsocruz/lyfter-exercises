import csv
import os

from src.logic.category import Category

'''Category'''


def convert_from_object_to_dictionary_category(list_of_categories=[]):
    try:
        list_of_dict = []
        for item in list_of_categories:
            #id = item.id
            name = item.name
            #list_of_dict.append({'id': id, 'category': name, })
            list_of_dict.append({'category': name })
        return list_of_dict
    except Exception as ex:
            print(f"ERROR - convert_from_object_to_dictionary_category: {ex}")


def convert_from_dictionary_to_object_category(list_of_dict=[]):
    try:
        list_of_objects = []
        for item in list_of_dict:
            name = item.get('category')
            list_of_objects.append(Category(name=name))
        return list_of_objects
    except Exception as ex:
            print(f"ERROR - convert_from_dictionary_to_object_category: {ex}")


def save_categories_info(file_name,data):
    #header_categories = ['id', 'category']
    header_categories = ['category']

    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = f'files/{file_name}.csv'
    file_path = os.path.join(script_dir, relative_path)

    try:
        if os.path.isfile(file_path):
            with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, header_categories)
                writer.writeheader()
                writer.writerows(data)
        else:
            with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, header_categories)
                writer.writeheader()
                writer.writerows(data)
        # print(f'\n¡Archivo exportado con éxito en "{file_path}"!')
    except IOError as ex:
        print(f"Error: Ocurrió un problema al escribir en el archivo.\n{ex}")
        pass
    except Exception as ex:
        print(f"Ocurrió un error inesperado: {ex}")
        pass


def load_categories_info():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/categories.csv'
    file_path = os.path.join(script_dir, relative_path)

    categories_list = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # By default when importing a CSV the dict will have only string values, so we must convert them to int values
                #row['id'] = int(row['id'])
                categories_list.append(row)
        # print('\nArchivo de categories importado con éxito')
        return categories_list
    except FileNotFoundError as ex:
        print(f'\n\033[31m¡Sin archivo que importar!\033[39m : {ex}')
        return categories_list


def delete_exported_CSV():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/categories.csv'
    file_path = os.path.join(script_dir, relative_path)
    try:
        os.path.isfile(file_path)
        os.remove(file_path)
        input('\nArchivo eliminado con éxito\nPresione cualquier tecla para volver al menú anterior\n')
    except FileNotFoundError:
        input(
            '\n\033[31m¡Sin archivo que eliminar!\033[39m\nPresione cualquier tecla para volver al menú anterior\n')
        pass


def get_categories_info():
    try:
        list_of_dict_categories = load_categories_info()
        list_categories = convert_from_dictionary_to_object_category(list_of_dict_categories)
        table_data = []
        for item in list_categories:
            
            table_row = item.name
            table_data.append(table_row)
        return table_data
    except Exception as ex:
        print(f'ERROR - get_categories_info: {ex}')




