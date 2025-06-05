import os
clear = lambda: os.system('clear')
clear()

print(f'---------------------------------- Ejercicio # 1----------------------------------')
#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def ejercicio1_1(value1, value2):
    return value1 + value2


def ejercicio1_2(value):
    return ejercicio1_1(value,value)/100
    

print("Test-> ",ejercicio1_2(100))
print(f'----------------------------------------------------------------------------------')


print('---------------------------------- Ejercicio # 2----------------------------------')
#Experimente con el concepto de scope: 
# 1. Intente accesar a una variable definida dentro de una función desde afuera. 
# Intente accesar a una variable global desde una función y cambiar su valor
global_variable = "Hello"
def ejercicio2_1():
    my_variable =0
def ejercicio2_2():
    global_variable="Green"
    print(global_variable)
    print(my_variable)
#ejercicio2_2()
print(f'----------------------------------------------------------------------------------\n')


print('---------------------------------- Ejercicio # 3----------------------------------')
    #3. Cree una función que retorne la suma de todos los números de una lista.
    #     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
def ejercicio3(list):
    sum = 0
    for element in list:
        sum = sum + element
    return sum
print(ejercicio3([4, 6, 2, 29]))
print(f'----------------------------------------------------------------------------------\n')


print('---------------------------------- Ejercicio # 4----------------------------------')
#Cree una función que le de la vuelta a un string y lo retorne.
def ejercicio4(my_word):
    word_changed=""
    for index in range(0,len(my_word)):
        word_changed = word_changed + my_word[len(my_word)-index-1]
    return word_changed
print("Hola Mundo -> ",ejercicio4("Hola Mundo"))
print(f'----------------------------------------------------------------------------------\n')




print('---------------------------------- Ejercicio # 5----------------------------------')
def ejercicio5(string):
#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string
    #There’s 3 upper cases and 13 lower cases
    counter_upper = 0 
    counter_lower = 0

    for index in range(0,len(string)):
        if(string[index]==" "):
            continue
        elif(string[index].isupper()):
            counter_upper+=1
        else:
            counter_lower+=1

    return f'In "{string}". There are {counter_upper} upper cases and {counter_lower} lower cases'
    
print(ejercicio5("I love Nación Sushi")) 
print(f'----------------------------------------------------------------------------------\n')



print('---------------------------------- Ejercicio # 6----------------------------------')
#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string


def separate_words(my_string): #Divides the strings in words and store them in a list

    word = ""
    limit = len(my_string)
    list_of_words = []

    for index, char in enumerate(my_string):
        if(index == limit-1):
            word = word + char
            list_of_words.append(word)
            word = ""
        elif(not char == "-"):
            word = word + char
        elif(char == "-"):
            list_of_words.append(word)
            word = ""

    return list_of_words


def bouble(list_of_words):

    generic_word = ""

    for i in range(0,len(list_of_words)):
        for j in range(0,len(list_of_words)-1):
            if(list_of_words[i] < list_of_words[j]):
                generic_word = list_of_words[i]
                list_of_words[i] = list_of_words[j]
                list_of_words[j] = generic_word

    return list_of_words 


def join_words(my_string):

    new_string = ""
    list_of_words = separate_words(my_string)
    ordered_words = bouble(list_of_words)

    for index in range(0,len(ordered_words)):
        new_string = f'{new_string}-{ordered_words[index]}'
    new_string = new_string[1:] #removing the first char of the string, otherwise it will start by "-"

    return new_string

                #“computadora-funcion-monitor-python-variable”


print(join_words("python-variable-funcion-computadora-monitor"))

print(f'----------------------------------------------------------------------------------\n')




print('---------------------------------- Ejercicio # 7----------------------------------')
#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma
def is_prime_number(number):
    counter=0
    is_prime = False
    for j in range(2,number+1):
        if(number%j==0):
            counter+=1
    if(counter==1):
        is_prime = True
    return is_prime


def ejercicio7(list_of_numbers):
    new_list_of_numbers=[]
    
    for element in list_of_numbers:
        if(is_prime_number(element)):
            new_list_of_numbers.append(element)
    return new_list_of_numbers 

print(ejercicio7([1, 4, 6, 7, 13, 9, 67]))

print(f'----------------------------------------------------------------------------------\n')
