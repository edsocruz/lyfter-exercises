from src.data.data_category import convert_from_object_to_dictionary_category, save_categories_info, load_categories_info, convert_from_dictionary_to_object_category
from src.data.data_transaction import load_transactions_info, convert_from_dictionary_to_object_transaction

from src.view.view_transactions_table import show_landing_window
from src.view.view_categories_table import show_categories_list

import os
def clear(): return os.system('clear')


def main():
    '''Import transactions'''
    list_of_dict_transactions = load_transactions_info()
    transactions_list = convert_from_dictionary_to_object_transaction(list_of_dict_transactions)
    show_landing_window(transactions_list)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
