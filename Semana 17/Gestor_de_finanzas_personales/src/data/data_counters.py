import csv
import os

'''Counters'''
#The purpose of this file is have the counters of each ID created, each column represents
#an ID, each time an object is created it'll have an ID assigned, those IDs shouldn't be 
#edited 

def save_id_counters(data):
    try:
        header_id_counters = ['category', 'transaction']

        script_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = 'files/id_counters.csv'
        file_path = os.path.join(script_dir, relative_path)

        #if os.path.isfile(file_path):
        #    with open(file_path, 'a', encoding='utf-8', newline='') as csvfile:
        #        writer = csv.DictWriter(csvfile, header_id_counters)
        #        writer.writerows(data)
        #else:
        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, header_id_counters)
            writer.writeheader()
            writer.writerows(data)
    except OSError as ex:
        print(f'ERROR - save_id_counters: {ex} ')

def load_id_counters_info():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'files/id_counters.csv'
    file_path = os.path.join(script_dir, relative_path)

    ids_list = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ## By default when importing a CSV the dict will have only string values, so we must convert them to float values
                row['category'] = int(row['category'])
                row['transaction'] = int(row['transaction'])
                ids_list.append(row)
        #print('\nArchivo de id_counters importado con éxito\nPresione cualquier tecla para volver al menú anterior\n')
        return ids_list
    except FileNotFoundError:
        print('\n\033[31m¡Sin archivo que importar!\033[39m')
        return ids_list

