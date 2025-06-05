import os
clear = lambda: os.system('clear')
clear()

def ejercicio1():
    print('---------------------------------- Ejercicio #1 ----------------------------------')
    #1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
    second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
    for index in range(0, len(first_list)):
        print(first_list[index],second_list[index])
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio2():
    print('---------------------------------- Ejercicio #2 ----------------------------------')
    my_string = 'Pizza con piña'
    #Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    for char in range(len(my_string)-1,-1,-1):
        print(my_string[char])
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio3():
    print('---------------------------------- Ejercicio #3 ----------------------------------')
    #Cree un programa que intercambie el primer y ultimo elemento de una lista. 
    #Debe funcionar con listas de cualquier tamaño
    my_list = [4, 3, 6, 1, 7]
    print(my_list)
    cup_of_tea = my_list[0]
    my_list[0] = my_list[len(my_list)-1]
    my_list[len(my_list)-1]= cup_of_tea
    print(my_list)
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio4():
    print('---------------------------------- Ejercicio #4 ----------------------------------')
    #Cree un programa que elimine todos los números impares de una lista.
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(my_list)
    for index,num in enumerate(my_list):
        if (num%2!=0):
            my_list.pop(index)
    print(my_list)
    print(f'----------------------------------------------------------------------------------\n')


def ejercicio5():
    print('---------------------------------- Ejercicio #5 ----------------------------------') 
    #Cree un programa que le pida al usuario 10 números,
    #  y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    #my_list = [86, 54, 23, 54, 67, 21, 2, 65, 10, 32 ]
    my_list = []
    user_number=0
    iterator=0
    generic_number=0
    while(iterator<10):
        user_number= int(input(f'Ingrese el valor #{iterator+1}: '))
        if(user_number>generic_number):
            generic_number=user_number
        my_list.append(user_number)
        iterator+=1
    print(f'Lista: {my_list}\nEl más alto fue: {generic_number}')
    print(f'----------------------------------------------------------------------------------\n')


ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()