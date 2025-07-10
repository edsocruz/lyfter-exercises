
# Cree un decorador que haga print de los parámetros y retorno de la
# función que decore.

def decorator_exercise_1(func):
    def wrapper(*arg):
        print('Parameters: ')
        for item in arg:
            print(item)
        result = func(*arg)
        print('Result: ',result)
        return result
    return wrapper


@decorator_exercise_1
def sum_numbers(*arg):
    result = 0
    for item in arg:
        result = result + item
    return result

@decorator_exercise_1
def multiply_numbers(*arg):
    result = 1
    for item in arg:
        result = result * item
    return result

print('Sumatory')
sum_numbers(1, 2,3,4,5,6,7,8,9,10)

print('\nMultiplication')
multiply_numbers(1, 2,3,4,5,6,7,8,9,10)
