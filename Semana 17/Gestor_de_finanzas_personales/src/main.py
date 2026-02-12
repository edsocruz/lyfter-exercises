from src.logic.finance_manager import load_and_convert_transactions_info
from src.view.view_transactions_table import show_landing_window

import os
def clear(): return os.system('clear')


def main():
    '''Import transactions'''
    transactions_list = load_and_convert_transactions_info()
    show_landing_window(transactions_list)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
