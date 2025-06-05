import os
clear = lambda: os.system('clear')
GREEN   = '\033[32m'
RESET   = '\033[39m'
BLUE    = '\033[34m'
RED     = '\033[31m'

def addition(number_1, number_2):
    result = (number_1+number_2)
    return result


def subtraction(number_1, number_2):
    result = (number_1-number_2)
    return result


def multiplication(number_1, number_2):
    result = (number_1*number_2)
    return result


def division(number_1, number_2):
    result = (number_1/number_2)
    return result


def show_menu(current_number=0, error_message='', color_option=''):
    menu_options = ['(d) Dividir', '(m) Multiplicar', '(r) Restar', '(s) Sumar']

    if(color_option=='d'):
        menu_options[0] = GREEN + menu_options[0] + RESET
    elif(color_option=='m'):
        menu_options[1] = GREEN + menu_options[1] + RESET
    elif(color_option=='r'):
        menu_options[2] = GREEN + menu_options[2] + RESET
    elif(color_option=='s'):
        menu_options[3] = GREEN + menu_options[3] + RESET

    print(f'\nResultado: {current_number}\n')
    for option in menu_options:
        print(option)
    print(f'(c) Borrar')
    print(f'(q) Salir del programa')
    print(f'{error_message}')


def operacion(number_1, operation, number_2):
    result = 0
    if(operation=='d'):
        result = division(number_1, number_2)
    elif(operation=='m'):
        result = multiplication(number_1, number_2)
    elif(operation=='r'):
        result = subtraction(number_1, number_2)
    elif(operation=='s'):
        result = addition(number_1, number_2)
    return result


def realizar_operacion():
    result=0 #This number will be shown in the menu, it`s the "current number"   
    user_input = ''
    number_1 = 0 #first term of the operation 
    number_2 = 0 #second term of the operation 
    flag_operation = False
    operation = '' #operation it self (+,-,*,/)
    error_message = '' 
    was_the_input_a_number = False 

    show_menu()

    while(not user_input == 'q'):
        error_message = ''
        was_the_input_a_number = False
        user_input = input(f'->: ')
        clear()

        try: 
            if(float(user_input)+1 and flag_operation == False): # a number 1 is added because if we evaluate a 0 number in a 'True or False' clause, the 0 will be taken as false, 0 is a valid 

                result = float(user_input) 
                number_1 = float(user_input)
                was_the_input_a_number = True

            elif(
                float(user_input)+1 and flag_operation == True):
                # we'll storage the input in the second number field if:
                #   a number is already stored in number_1 and
                #   and an operation was selected 
                # otherwise the input will overwrite number_1
                
                number_2 = float(user_input)
                was_the_input_a_number = True

                if(number_2 == 0 and operation == 'd'):
                    number_2 = 0
                    flag_operation = False
                    raise ZeroDivisionError(RED+'\nNo puedes dividir un número entre 0\n'+RESET)
                
                result = operacion(number_1,operation,number_2)
                number_1 = result
                flag_operation = False

        except ValueError:
            pass
        except ZeroDivisionError as ex:
            error_message = ex

        try:
            if(was_the_input_a_number == False):
                if(user_input=='c'):
                    number_1 = 0
                    flag_operation = False
                    result = 0
                elif(user_input == 'd' or user_input == 'm' or user_input == 'r' or user_input == 's' or user_input == 'q'):
                    operation = user_input
                    flag_operation = True
                elif(user_input==''):
                    raise ValueError('\nDebes seleccionar una opcion para continuar\n')
                else:
                    raise ValueError(RED+'\nEsa opción no se corresponde con ninguna opcion\n'+RESET)
                
        except ValueError as ex:
            error_message = ex
        show_menu(current_number=result,error_message=error_message,color_option=user_input)

    if(user_input=='q'):
        exit()
    


def main():
    number = realizar_operacion()
    show_menu(number)



if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
	    print(f'An unexpected error occurred: {ex}')
