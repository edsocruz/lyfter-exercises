# Cree un decorador que se encargue de revisar si todos los
# parámetros de la función que decore son números, y arroje una excepción de no ser así.


def check_if_number(func):
    def wrapper(*arg, **kwargs):
        no_numeric_elements = []
        for item in arg:
            if (isinstance(item, (int, float))):
                print(f'{item} is a number')
            else:
                no_numeric_elements.append(item)
        if(no_numeric_elements.__len__!=0):
            raise ValueError(f'El argumento <{no_numeric_elements}> no es un número, \n')

        result = func(*arg, **kwargs)

        return result #si hay que modificar o agregar parametros se puede poner este segundo return 
    return wrapper


@check_if_number
def print_numbers(*arg):
    list_of_numbers = []
    for item in arg:
        list_of_numbers.append(item)
    print('\nList of numbers: ', list_of_numbers)


if __name__ == '__main__':
    try:
        print_numbers(1, 2, -3, 4, 'hdfd', 5, '600', 7, '0008')
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
