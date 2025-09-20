def bubble_sort(list_of_numbers: list):
    if not isinstance(list_of_numbers, list):
        raise TypeError('El elemento dado no es una lista')
    list_length = len(list_of_numbers)
    if list_length == 0:
        return list_of_numbers
    for j in range(0, list_length-1):
        any_change = False
        for i in range(0, len(list_of_numbers)-1-j):
            current_element = list_of_numbers[i]
            next_element = list_of_numbers[i+1]
            if (current_element > next_element):
                list_of_numbers[i] = next_element
                list_of_numbers[i+1] = current_element
                any_change = True
        if not any_change:
            break
    return list_of_numbers


# Ejercicio 2
'''---------------------------------- Ejercicio # 3----------------------------------'''
# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).


def ejercicio3(list):
    sum = 0
    for element in list:
        sum = sum + element
    return sum


print(ejercicio3([4, 6, 2, 29]))


'''---------------------------------- Ejercicio # 4----------------------------------'''
# Cree una función que le de la vuelta a un string y lo retorne.


def ejercicio4(my_word):
    word_changed = ""
    for index in range(0, len(my_word)):
        word_changed = word_changed + my_word[len(my_word)-index-1]
    return word_changed


print("Hola Mundo -> ", ejercicio4("Hola Mundo"))


'''---------------------------------- Ejercicio # 5----------------------------------'''


def ejercicio5(string):
    # Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string
    # There’s 3 upper cases and 13 lower cases
    counter_upper = 0
    counter_lower = 0

    for index in range(0, len(string)):
        if (string[index] == " "):
            continue
        elif (string[index].isupper()):
            counter_upper += 1
        else:
            counter_lower += 1

    return f'In "{string}". There are {counter_upper} upper cases and {counter_lower} lower cases'


print(ejercicio5("I love Nación Sushi"))


'''---------------------------------- Ejercicio # 6----------------------------------'''
# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string


def separate_words(my_string):  # Divides the strings in words and store them in a list

    word = ""
    limit = len(my_string)
    list_of_words = []

    for index, char in enumerate(my_string):
        if (index == limit-1):
            word = word + char
            list_of_words.append(word)
            word = ""
        elif (not char == "-"):
            word = word + char
        elif (char == "-"):
            list_of_words.append(word)
            word = ""

    return list_of_words


def bouble(list_of_words):

    generic_word = ""

    for i in range(0, len(list_of_words)):
        for j in range(0, len(list_of_words)-1):
            if (list_of_words[i] < list_of_words[j]):
                generic_word = list_of_words[i]
                list_of_words[i] = list_of_words[j]
                list_of_words[j] = generic_word

    return list_of_words


def join_words(my_string):

    new_string = ""
    list_of_words = separate_words(my_string)
    ordered_words = bouble(list_of_words)

    for index in range(0, len(ordered_words)):
        new_string = f'{new_string}-{ordered_words[index]}'
    # removing the first char of the string, otherwise it will start by "-"
    new_string = new_string[1:]

    return new_string

    # “computadora-funcion-monitor-python-variable”


print(join_words("python-variable-funcion-computadora-monitor"))


'''---------------------------------- Ejercicio # 7----------------------------------'''
# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma


def is_prime_number(number):
    counter = 0
    is_prime = False
    for j in range(2, number+1):
        if (number % j == 0):
            counter += 1
    if (counter == 1):
        is_prime = True
    return is_prime


def ejercicio7(list_of_numbers):
    new_list_of_numbers = []
    for element in list_of_numbers:
        if (is_prime_number(element)):
            new_list_of_numbers.append(element)
    return new_list_of_numbers


class EjercicioExtra1:
    def __init__(self):
        pass

    def addition(self, number1, number2):
        return number1+number2

    def average(self, list_of_numbers: list):
        sum_of_elements = 0
        amount_of_elements = len(list_of_numbers)
        for item in list_of_numbers:
            sum_of_elements += item
        return sum_of_elements/amount_of_elements

    def pass_celsius_to_fahrenheit(self, celsius):
        return (celsius*(9/5))+32

'''Ejercicio extra 3'''
def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

'''Ejercicio extra 4'''
def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()