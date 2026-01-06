import FreeSimpleGUI as sg
from datetime import date, datetime
from src.data.data_category import get_categories_info
from src.view.view_categories_table import view_show_categories_list
from src.logic.transaction import Transaction
from src.logic.category import Category
from src.logic.finance_manager import load_and_convert_transactions_info, convert_and_save_transactions_info, filter_by_date, validation_initial_date, validation_final_date
from src.data.data_transaction import data_export_csv, get_transactions_info


def show_landing_window(list_transactions=list):
    table_data = []
    filtered_by_date_flag = False

    for item in list_transactions:
        table_row = [item.id, item.type, item.title, item.amount, item.category.name, item.date.strftime("%d/%m/%Y")]
        table_data.append(table_row)

    # Declarar los elementos
    layout = [
        [sg.Text("Movimientos recientes",  font='_ 20'), sg.Push(), sg.Button("Filtrar por fecha", font='_ 12',key='-filtrar-')],
        [sg.Table(table_data, headings=[" Id ", "Tipo", "Título", "Monto", "Categoría", "Fecha"], auto_size_columns=True, font='_ 12', key='-transaction table-')],
        [sg.Push(), sg.Button("Añadir gasto",  font='_ 12'), sg.Button("Añadir ingreso", font='_ 12'), sg.Button("Crear categoría", font='_ 12'), sg.Push(), sg.Button("Exportar CSV", font='_ 12')],
    ]

    # Crear la ventana
    window = sg.Window("Gestor de finanzas personales", layout)

    # Event Loop para procesar "events" y obtener los "values" de los inputs
    while True:
        event, values = window.read()
        # Procesar el evento del cerrar la ventaja
        # (si el usuario lo hace)
        if event == sg.WIN_CLOSED:
            break
        elif event == "Añadir gasto":
            list_transactions = load_and_convert_transactions_info()
            view_add_transaction('Gasto', list_transactions)

            # Update the table with the new entry
            table_data = get_transactions_info()
            window['-transaction table-'].update(table_data)

        elif event == "Añadir ingreso":
            list_transactions = load_and_convert_transactions_info()
            view_add_transaction('Ingreso', list_transactions)

            # Update the table with the new entry
            table_data = get_transactions_info()
            window['-transaction table-'].update(table_data)

        elif event == "Crear categoría":
            view_show_categories_list()
            
        elif event == '-filtrar-':
            if not filtered_by_date_flag:
                filtered_table = filter_by_date(table_data)
                window['-transaction table-'].update(filtered_table)
                window['-filtrar-'].update('Resetrar')
                filtered_by_date_flag = True
            else:
                window['-transaction table-'].update(table_data)
                window['-filtrar-'].update('Filtrar por fehca')
                filtered_by_date_flag = False

        elif event == 'Exportar CSV':
            data_export_csv()
            sg.popup('Archivo exportado en la carpeta de descargas',  font='_ 12')
    window.close()


def show_filter_by_date():
    fecha_seleccionada_inicial = date.today()
    fecha_seleccionada_final = date.today()

    # Declarar los elementos
    layout = [
        [sg.Push(), sg.Text("Seleccione las fechas",  font='_ 20'), sg.Push()],
        [sg.Push(), sg.Button("Desde",  font='_ 12'), sg.Text("dd/mm/yyy ",  font='_ 12', key='-fecha inicio-'), sg.Push(),
         sg.Button("Hasta",  font='_ 12'), sg.Text("dd/mm/yyyy ",  font='_ 12', key='-fecha fin-'), sg.Push()],
        [sg.Push(), sg.Button("Filtrar",  font='_ 12'), sg.Push()],
    ]

    # Crear la ventana
    window = sg.Window("Filtrar por fechas", layout)

    # Event Loop para procesar "events" y obtener los "values" de los inputs
    flag_desde = False
    flag_hasta = False
    while True:
        event, values = window.read()
        # Procesar el evento del cerrar la ventana
        if event == sg.WIN_CLOSED:
            break
        elif event == "Desde":
            initial_date = sg.popup_get_date()
            if initial_date and isinstance(initial_date, tuple):
                validation_initial_date_result = validation_initial_date(window,initial_date)
                if validation_initial_date_result:
                    flag_desde, fecha_seleccionada_inicial = validation_initial_date_result
        elif event == "Hasta":
            final_date = sg.popup_get_date()
            if final_date and isinstance(final_date, tuple):
                validation_final_date_result = validation_final_date(window,fecha_seleccionada_inicial, final_date)
                if validation_final_date_result:
                    flag_hasta, fecha_seleccionada_final = validation_final_date_result

        elif event == 'Filtrar':
            if flag_desde and flag_hasta:
                dates = [fecha_seleccionada_inicial,fecha_seleccionada_final]
                window.close()
                return dates
            else:
                sg.popup_error('Para filtrar debes elegir la fecha de inicio y la fecha de fin',  font='_ 12')
    window.close()


def view_add_transaction(type: str, list_transactions=list):

    # Declarar los elementos
    # it returns a list of list with the attribute of a category [[name],[name],[name]...]
    categories = get_categories_info()
    date = 'mm/dd/yyyy'

    layout = [
        [sg.Text('Complete la información del movimiento',  font='_ 20')],
        [sg.Text('Nombre: ',  font='_ 12'),
        sg.Input(key='-NAME-',  font='_ 12')],
        [sg.Text('Monto: ',  font='_ 12'), sg.Input(
            key='-AMOUNT-',  font='_ 12')],
        [sg.Text('Categoría: ',  font='_ 12'), sg.Combo(
            categories, key='-CATEGORY-', font='_ 12')],
        [sg.Button("Escoger fecha", font='_ 12'), sg.Text(
            f'Fecha: {date}', key='-DATE-', font='_ 12'), ],
        [sg.Push(), sg.Button("Agregar"), sg.Button("Cancelar"), sg.Push()],
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
        elif event == "Escoger fecha":
            date = sg.popup_get_date()
            formatted_date = f'{date[1]}/{date[0]}/{date[2]}'
            window['-DATE-'].update(formatted_date)
        elif event == "Agregar":
            formatted_date = f'{date[1]}/{date[0]}/{date[2]}'
            name = values['-NAME-']
            amount = int(values['-AMOUNT-'])
            category = values['-CATEGORY-']
            new_object_transaction = Transaction(type=type, title=name, amount=amount, category=Category(category), date=formatted_date)
            # We add the new transaction to the list
            list_transactions.append(new_object_transaction)
            # Now we export that list and overwrite the CSV with the new info
            convert_and_save_transactions_info(list_transactions)
            break
    window.close()
