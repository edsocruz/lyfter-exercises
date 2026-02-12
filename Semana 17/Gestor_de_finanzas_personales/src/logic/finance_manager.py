from src.data.data_transaction import  convert_from_object_to_dictionary_transaction, save_transactions_info, load_transactions_info, convert_from_dictionary_to_object_transaction, get_transactions_info
from datetime import date, datetime
import FreeSimpleGUI as sg



def load_and_convert_transactions_info():
    list_of_dict_transactions = load_transactions_info()
    return convert_from_dictionary_to_object_transaction(list_of_dict_transactions)


def convert_and_save_transactions_info(list_transactions):
    list_of_dict_transactions = convert_from_object_to_dictionary_transaction(list_transactions)
    save_transactions_info(list_of_dict_transactions)
    

def filter_by_date(table_data):
    from src.view.view_transactions_table import show_filter_by_date # here we have a local import to avoid circular import errors
    filtered_table = []
    filter_dates = show_filter_by_date()
    initial_date = filter_dates[0]
    final_date = filter_dates[1]
    for item in table_data:
        fecha_str = item[-1]
        fecha_obj = datetime.strptime(fecha_str, '%d/%m/%Y').date()
        if (initial_date <= fecha_obj) and (fecha_obj <= final_date):
            filtered_table.append(item)
    return filtered_table

def formatted_date(initial_date):
    return f'{initial_date[1]}/{initial_date[0]}/{initial_date[2]}'

def validation_initial_date(window, initial_date):
    if initial_date:
        date_dd_mm_yyyy = formatted_date(initial_date)   # Formatear la fecha seleccionada
        fecha_seleccionada_inicial = date(initial_date[2], initial_date[0], initial_date[1])  # Crear objeto date para la fecha seleccionada
        fecha_actual = date.today() # Obtener la fecha actual
        if fecha_seleccionada_inicial > fecha_actual:   # Comparar fechas
            sg.popup_error(
                'No puedes seleccionar una fecha futura. Intenta de nuevo.',  font='_ 12')
            return None
        else:
            window['-fecha inicio-'].update(date_dd_mm_yyyy)
            return [True, fecha_seleccionada_inicial]
    return None

def validation_final_date(window, fecha_seleccionada_inicial, final_date):
    if final_date:
        date_dd_mm_yyyy = formatted_date(final_date)   # Formatear la fecha seleccionada
        fecha_seleccionada_final = date(final_date[2], final_date[0], final_date[1])  # Crear objeto date para la fecha seleccionada
        fecha_actual = date.today() # Obtener la fecha actual
        if fecha_seleccionada_final > fecha_actual:   # Comparar fechas
            sg.popup_error(
                'No puedes seleccionar una fecha futura. Intenta de nuevo.',  font='_ 12')
            return None
        elif fecha_seleccionada_inicial > fecha_seleccionada_final:
            sg.popup_error('La fecha de inicio no puede ser mayor que la fecha final',  font='_ 12')
            return None
        else:
            window['-fecha fin-'].update(date_dd_mm_yyyy)
            return [True, fecha_seleccionada_final]
    return None