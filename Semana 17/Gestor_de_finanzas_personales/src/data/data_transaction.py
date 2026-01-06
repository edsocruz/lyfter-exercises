import csv
import os
from pathlib import Path
import platform
import shutil

from src.logic.transaction import Transaction
from src.logic.category import Category

'''Transaction'''


def convert_from_object_to_dictionary_transaction(list_of_objects_transactions=[]):
    try:
        list_of_dict = []
        for item in list_of_objects_transactions:
            id = item.id
            type = item.type
            title = item.title
            amount = item.amount
            # Here we must save only the category name, otherwise it'll save the object memory location
            category = item.category.name
            date = item.date.strftime("%d/%m/%Y")
            list_of_dict.append({'id': id, 'type': type, 'title': title,
                                'amount': amount, 'category': category, 'date': date})
        return list_of_dict
    except Exception as ex:
            print(f"ERROR - convert_from_object_to_dictionary_transaction: {ex}")


def convert_from_dictionary_to_object_transaction(list_of_dict=[]):
    try:
        list_of_objects = []
        for item in list_of_dict:
            id = int(item.get('id'))
            type = item.get('type')
            title = item.get('title')
            amount = int(item.get('amount'))
            category = item.get('category')
            date = item.get('date')
            list_of_objects.append(Transaction(
                id=id, type=type, title=title, amount=amount, category=Category(category), date=date))
        return list_of_objects
    except Exception as ex:
            print(f"ERROR - convert_from_dictionary_to_object_transaction: {ex}")


def save_transactions_info(data):
    header_categories = ['id', 'type', 'title', 'amount', 'category', 'date']

    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/transactions.csv'
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


def get_downloads_folder():
    # Obten el directorio de inicio
    home = str(Path.home())
    # Determinar la carpeta de descargas en función del sistema operativo
    if platform.system() == "Windows":
        # Para Windows
        downloads_folder = os.path.join(home, "Downloads")
    else:
        # Para Mac y Linux (en su mayoría tienen la carpeta "Downloads")
        downloads_folder = os.path.join(home, "Downloads")
    return downloads_folder


def data_export_csv():
    destino = get_downloads_folder()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/transactions.csv'
    origen = os.path.join(script_dir, relative_path)

    try:
        # Asegurarse de que la ruta de destino es un directorio existente
        if os.path.isdir(destino):
            # Si el destino es un directorio, agrega el nombre del archivo al final
            destino = os.path.join(destino, os.path.basename(origen))

        # Copiar el archivo
        shutil.copy(origen, destino)
        print(f"Archivo copiado a: {destino}")
    except FileNotFoundError as e:
        print(f"Error: {e}. El archivo o directorio mencionado no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def load_transactions_info():
    transactions_list = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/transactions.csv'
    file_path = os.path.join(script_dir, relative_path)
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # By default when importing a CSV the dict will have only string values, so we must convert them to int values
                row['id'] = int(row['id'])
                transactions_list.append(row)
        # print('\nArchivo de categories importado con éxito')
        return transactions_list
    except FileNotFoundError:
        print('\n\033[31m¡Sin archivo que importar!\033[39m')
        return transactions_list


def delete_exported_CSV():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/transactions.csv'
    file_path = os.path.join(script_dir, relative_path)
    try:
        os.path.isfile(file_path)
        os.remove(file_path)
        print('\nArchivo eliminado con éxito')
    except FileNotFoundError:
        print(
            '\n\033[31m¡Sin archivo que eliminar!\033[39m')
        pass


def get_transactions_info():
    try:
        list_of_dict_transactions = load_transactions_info()
        list_transactions = convert_from_dictionary_to_object_transaction(list_of_dict_transactions)
        table_data = []
        for item in list_transactions:
            table_row = [item.id, item.type, item.title, item.amount, item.category.name, item.date]
            table_data.append(table_row)
        return table_data
    except Exception as ex:
        print(f'ERROR - get_transactions_info: {ex}')
