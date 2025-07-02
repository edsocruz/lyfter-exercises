import csv
import os
from student import Student


def convert_from_object_to_dictionary(list_of_objects=[]):
    list_of_dict = []
    for item in list_of_objects:
        name = item.name
        section = item.section
        spanish_grade = item.spanish_grade
        english_grade = item.english_grade
        social_studies_grade = item.social_studies_grade
        science_grade = item.science_grade
        average_grade = item.average_grade
        list_of_dict.append({'name': name, 'section': section, 'spanish_grade': spanish_grade, 'english_grade': english_grade,
                        'social_studies_grade': social_studies_grade, 'science_grade': science_grade, 'average_grade': average_grade})

    return list_of_dict

def convert_from_dictionary_to_object(list_of_dict=[]):
    list_of_objects = []
    for item in list_of_dict:
        name = item.get('name')
        section = item.get('section')
        spanish_grade = item.get('spanish_grade')
        english_grade = item.get('english_grade')
        social_studies_grade = item.get('social_studies_grade')
        science_grade = item.get('science_grade')
        average_grade = item.get('average_grade')
        list_of_objects.append(Student(name,section,spanish_grade,english_grade,social_studies_grade,science_grade,average_grade))
    return list_of_objects

def save_students_info(path, data, headers):
    try:
        with open(path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, headers)
            writer.writeheader()
            writer.writerows(data)
        input(
            f'\n¡Archivo exportado con éxito en "{path}"!\nPresione cualquier tecla para volver al menú anterior\n')
    except IOError:
        print("Error: Ocurrió un problema al escribir en el archivo.")
        pass
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        pass


def load_students_info(path):
    students_list = []
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # By default when importing a CSV the dict will have only string values, so we must convert them to float values
                row['spanish_grade'] = float(row['spanish_grade'])
                row['english_grade'] = float(row['english_grade'])
                row['social_studies_grade'] = float(
                    row['social_studies_grade'])
                row['science_grade'] = float(row['science_grade'])
                row['average_grade'] = float(row['average_grade'])
                students_list.append(row)
        input('\nArchivo importado con éxito\nPresione cualquier tecla para volver al menú anterior\n')
        return students_list
    except FileNotFoundError:
        input(
            '\n\033[31m¡Sin archivo que importar!\033[39m\nPresione cualquier tecla para volver al menú anterior\n')
        return students_list


def delete_exported_CSV(path):
    try:
        os.path.isfile(path)
        os.remove(path)
        input('\nArchivo eliminado con éxito\nPresione cualquier tecla para volver al menú anterior\n')
    except FileNotFoundError:
        input(
            '\n\033[31m¡Sin archivo que eliminar!\033[39m\nPresione cualquier tecla para volver al menú anterior\n')
        pass
