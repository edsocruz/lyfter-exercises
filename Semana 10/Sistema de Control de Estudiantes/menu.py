import os
#from actions import calculate_average_grade

## Tengo un bug cuando importo un archivo vacio y luego trato de ver los estudiantes (opcion 2)

def clear_console():
    return os.system('clear')


def show_landing_menu(error_message=''):
    print("┌──────────────────────────────────────────────────────────┐")
    print('│   \u2605 Bienvenido al Sistema de Control de Estudiantes \u2605    │')
    print("├──────────────────────────────────────────────────────────┤")
    print('│   1. Ingresar informacion de estudiantes                 │')
    print('│   2. Ver todos los estudiantes ingresados en el sistema  │')
    print('│   3. Ver top 3 de los mejores estudiantes                │')
    print('│   4. Ver la nota promedio global                         │')
    print('│   5. Exportar todos los datos a un archivo CSV           │')
    print('│   6. Importar todos los datos desde un archivo CSV       │')
    print('│   7. Eliminar los datos exportados previamente en un CSV │')
    print('│   8. Salir del programa                                  │')
    print('│                                                          │')
    print("└──────────────────────────────────────────────────────────┘")
    user_input = input(f"{error_message}✦ Elige una opción del menú (1-8) ➔ ")
    return user_input


def request_spanish_grade():
    try:
        spanish_grade = float(input('    Nota de español \u2794 '))
        if spanish_grade < 0 or spanish_grade > 100:
            raise ValueError
    except ValueError:
            input('\033[31m    La nota de español debe ser un número entre 0 a 100 \033[39m')
            spanish_grade = request_spanish_grade()
            pass
    return spanish_grade


def request_english_grade():
    try:
        english_grade = float(input('    Nota de ingles \u2794 '))
        if english_grade < 0 or english_grade > 100:
            raise ValueError
    except ValueError:
            input('\033[31m    La nota de ingles debe ser un número entre 0 a 100 \033[39m')
            english_grade = request_english_grade()
            pass
    return english_grade


def request_social_studies_grade():
    try:
        social_studies_grade = float(input('    Nota de sociales \u2794 '))
        if social_studies_grade < 0 or social_studies_grade > 100:
            raise ValueError
    except ValueError:
            input('\033[31m    La nota de sociales debe ser un número entre 0 a 100 \033[39m')
            social_studies_grade = request_social_studies_grade()
            pass
    return social_studies_grade


def request_science_grade():
    try:
        science_grade = float(input('    Nota de ciencias \u2794 '))
        if science_grade < 0 or science_grade > 100:
            raise ValueError
    except ValueError:
            input('\033[31m    La nota de ciencias debe ser un número entre 0 a 100 \033[39m')
            science_grade = request_science_grade()
            pass
    return science_grade



def request_student_info():
    print('\n \u2606 Para registrar un estudiante digite la siguiente información\n')
    name = input('    Nombre completo \u2794 ')
    section = input('    Sección \u2794 ')
    spanish_grade = request_spanish_grade()
    english_grade = request_english_grade()
    social_studies_grade = request_social_studies_grade()
    science_grade = request_science_grade()
    average_grade = (spanish_grade + english_grade + social_studies_grade + science_grade) / 4
    student = {'name': name, 'section': section, 'spanish_grade': spanish_grade, 'english_grade': english_grade,
                'social_studies_grade': social_studies_grade, 'science_grade': science_grade, 'average_grade':average_grade}

    return student


def show_student_info(name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade):
    print(f'\n \u25A0 Nombre completo   \u2794 {name}')
    print(f' \u25A1 Sección           \u2794 {section}')
    print(f' \u25CB Nota de español   \u2794 {spanish_grade}')
    print(f' \u25CB Nota de ingles    \u2794 {english_grade}')
    print(f' \u25CB Nota de sociales  \u2794 {social_studies_grade}')
    print(f' \u25CB Nota de ciencias  \u2794 {science_grade}')
    print(f' \u2605 Nota promedio     \u2794 {average_grade}')


def show_all_students_info(list_of_students = []):
    print('\nLista de estudiantes registrados en el sistema')
    for student in list_of_students:
        show_student_info(student.get('name'),student.get('section'),student.get('spanish_grade'),student.get('english_grade'),student.get('social_studies_grade'),student.get('science_grade'),student.get('average_grade'))

# it receives 3 arrays, in the array the information of one student
def show_top_3_students(sorted_students_list=[]):
    clear_console()
    print('')
    print("┌────────────────────────────────────────────────────────┐")
    print('│             \u2605 Top 3 mejores estudiantes \u2605              │')
    print("└────────────────────────────────────────────────────────┘")
    print('\nPrimer lugar')
    show_student_info(sorted_students_list[0].get('name'),sorted_students_list[0].get('section'),sorted_students_list[0].get('spanish_grade'),sorted_students_list[0].get('english_grade'),sorted_students_list[0].get('social_studies_grade'),sorted_students_list[0].get('science_grade'),sorted_students_list[0].get('average_grade'))
    print('\nSegundo lugar')
    show_student_info(sorted_students_list[1].get('name'),sorted_students_list[1].get('section'),sorted_students_list[1].get('spanish_grade'),sorted_students_list[1].get('english_grade'),sorted_students_list[1].get('social_studies_grade'),sorted_students_list[1].get('science_grade'),sorted_students_list[1].get('average_grade'))
    print('\nTercer lugar')
    show_student_info(sorted_students_list[2].get('name'),sorted_students_list[2].get('section'),sorted_students_list[2].get('spanish_grade'),sorted_students_list[2].get('english_grade'),sorted_students_list[2].get('social_studies_grade'),sorted_students_list[2].get('science_grade'),sorted_students_list[2].get('average_grade'))
    input('\nPresione enter para volver al menú anterior\n')


def show_average_grade(grade=0):
    print(f"┌────────────────────────────────────────────────────────┐")
    print(f'             La nota promedio global es de: {grade}           ')
    print(f"└────────────────────────────────────────────────────────┘")
    input('\nPresione enter para volver al menú anterior\n')
