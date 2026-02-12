import FreeSimpleGUI as sg
from src.logic.category import Category
from src.data.data_category import convert_from_object_to_dictionary_category,save_categories_info, load_categories_info, convert_from_dictionary_to_object_category, get_categories_info


def view_show_categories_list():
    table_data = get_categories_info()

    # Declarar los elementos
    layout = [
        [sg.Text("Categorias registradas",  font='_ 20')],
        [sg.Table(table_data, headings=["       Nombre       "], key='-categories table-', font='_ 12')],
        [sg.Push(),sg.Button("Agregar categoría"), sg.Button("Cancelar"), sg.Push(),],
    ]

    # Crear la ventana
    window = sg.Window("Gestor de finanzas personales", layout)

    # Event Loop para procesar "events" y obtener los "values" de los inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Cancelar":
            break
        elif event == "Agregar categoría":
            list_of_dict_categories = load_categories_info()
            list_categories = convert_from_dictionary_to_object_category(list_of_dict_categories)
            view_add_category(list_categories)
            #Update the table with the new category
            table_data = get_categories_info()
            window['-categories table-'].update(table_data)

    window.close()


def view_add_category(list_categories=list):

    # Declarar los elementos
    layout = [
        [sg.Text('Digite el nombre de la nueva categoría',  font='_ 20')],
        [sg.Input(key='-NEW CATEGORY-',  font='_ 12')],
        [sg.Push(),sg.Button("Agregar"), sg.Button("Cancelar"),sg.Push()],
    ]

    # Crear la ventana
    window = sg.Window("Gestor de finanzas personales", layout)

    # Event Loop para procesar "events" y obtener los "values" de los inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Cancelar":
            break
        elif event == "Agregar":
            category_name = values['-NEW CATEGORY-']
            #We add the new category to the list 
            list_categories.append(Category(category_name))
            #Now we export that list and overwrite the CSV with the new info
            list_of_dict_categories = convert_from_object_to_dictionary_category(list_categories)
            save_categories_info('categories',list_of_dict_categories)
            break
    window.close()






