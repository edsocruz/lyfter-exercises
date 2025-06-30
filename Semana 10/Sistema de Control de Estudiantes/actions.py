from menu import clear_console, show_landing_menu, request_student_info, show_student_info, show_top_3_students, show_average_grade, show_all_students_info
from Data.data import save_students_info, load_students_info, delete_exported_CSV
import os
# con este metodo era que estaba teniendo una dependencia infinita con el modulo de menu


def calculate_average_grade(spanish_grade, english_grade, social_studies_grade, science_grade):
    average_grade = (spanish_grade + english_grade +
                    social_studies_grade + science_grade) / 4
    return average_grade


def calculate_global_average_grade(students_list=[]):
    sum_of_items = 0
    count_of_items = 0
    global_average_grade = 0
    for index, item in enumerate(students_list):
        sum_of_items = sum_of_items + item.get('average_grade')
        count_of_items = index + 1
    if count_of_items == 0:
        global_average_grade = 0
    else:
        global_average_grade = sum_of_items/count_of_items
    # number truncated with two decimals
    return "{:.2f}".format(global_average_grade)


def bubble(students_list=[]):
    generic_student = {}
    for i in range(0, len(students_list)):
        for j in range(0, len(students_list)-1):
            if (students_list[i].get('average_grade') > students_list[j].get('average_grade')):
                generic_student = students_list[i]
                students_list[i] = students_list[j]
                students_list[j] = generic_student
    return students_list


def calculate_best_3_students(students_list=[]):
    sorted_students = bubble(students_list)
    student_1 = sorted_students[0]
    student_2 = sorted_students[1]
    student_3 = sorted_students[2]
    best_3_students = [student_1, student_2, student_3]
    return best_3_students


def control():
    user_input = ''
    students_header = ['name', 'section', 'spanish_grade', 'english_grade',
                    'social_studies_grade', 'science_grade', 'average_grade']
    students_list = []

    # Here we can manage the CVS' path and use the same one in all methods that modifies the CVS file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = 'Data/students.csv'
    file_path = os.path.join(script_dir, relative_path)

    while (not user_input == '8'):
        clear_console()
        user_input = show_landing_menu()

        if user_input == '1':
            add_another_student = 's'
            while add_another_student == 's':
                clear_console()
                student = request_student_info()
                students_list.append(student)
                add_another_student = input('\n \u25CB Si desea ingresar otro estudiante digite "s", de lo contrario digite cualquier tecla \u2794 ')
        elif user_input == '2':
            clear_console()
            show_all_students_info(students_list)
            input('\nPresione cualquier tecla para volver al menú anterior\n')
        elif user_input == '3':
            try:
                sorted_students_list = calculate_best_3_students(students_list)
                show_top_3_students(sorted_students_list)
            except IndexError:
                input('\nSe necesitan mínimo 3 estudiantes registrados en el sistema para poder ver este registro ')
                pass
        elif user_input == '4':
            clear_console()
            global_average_grade = calculate_global_average_grade(
                students_list)
            show_average_grade(global_average_grade)
        elif user_input == '5':
            clear_console()
            save_students_info(file_path, students_list, students_header)
        elif user_input == '6':
            clear_console()
            students_list = load_students_info(file_path)
        elif user_input == '7':
            clear_console()
            delete_exported_CSV(file_path)
        elif user_input == '8':
            exit()
