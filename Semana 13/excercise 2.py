# Cree un decorador que se encargue de revisar si todos los
# parámetros de la función que decore son números, y arroje una excepción de no ser así.


def check_if_number(func):
    def wrapper(*arg):
        print('\n')
        for item in arg:
            try:
                if (float(item)):
                    print(f'{item} is a number')
            except ValueError as ex:
                print(f'El argumento <{item}> no es un número, \nError: {ex}')

        result = func(*arg)

        return result
    return wrapper


@check_if_number
def print_numbers(*arg):
    list_of_numbers= []
    for item in arg:
        list_of_numbers.append(item)
    print('\nList of numbers: ',list_of_numbers)

print_numbers(1, '2', -3, 'dfg', 5, '600', 7, '0008', '87fds', 10, '0.0000004')

