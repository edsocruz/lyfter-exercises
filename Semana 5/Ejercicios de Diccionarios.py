import os
clear = lambda: os.system('clear')
clear()


def ejercicio1():
    print('---------------------------------- Ejercicio #1 ----------------------------------')
    #Cree un diccionario que guarde la siguiente información sobre un hotel: 
    # - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    #     - `numero`
    #     - `piso`
    #     - `precio_por_noche`
    
    my_dictionary = {
    'nombre':'Hilton',
    'numero_de_estrellas':4,
    'habitaciones': [
        {
            'numero':'1',
            'piso':1,
            'precio_por_noche':100
        },
        {
            'numero':'2',
            'piso':2,
            'precio_por_noche':150
        },
        {
            'numero':'3',
            'piso':3,
            'precio_por_noche':200
        },
    ]
    }
    for key,values in my_dictionary.items():
        print(f'{key} -> {values}')

    print(f'----------------------------------------------------------------------------------\n')

def ejercicio2():
    print('---------------------------------- Ejercicio #2 ----------------------------------')
    #Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values
    list_a = ['first_name', 'last_name', 'role']
    list_b = ['Alek', 'Castillo', 'Software Engineer']
    my_dictionary={}
    for index,element in enumerate(list_a):
        my_dictionary[element]=list_b[index]
    print(my_dictionary)
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio3():
    print('---------------------------------- Ejercicio 3# ----------------------------------')
    #Cree un programa que use una lista para eliminar keys de un diccionario.
    list_of_keys = ['access_level', 'age']
    employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
    for element in list_of_keys:
        employee.pop(f'{element}')
    print(employee)
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio_extra_1():
    print('---------------------------------- Ejercicio 4# ----------------------------------')
    #Cree un diccionario que guarde el total de ventas de cada UPC.

    sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
    ]
    result={}
    for sale in sales:
        list_of_items = sale.get("items") # stores in a variable the items of each sale in a dictionary
        for item in list_of_items: #iterates the new dictionary
            if(not result.get(item.get("upc"))): #if the value does not exist we add it to the dictionary
                result[item.get("upc")]=item.get("unit_price")
            else:
                old_value=result.pop(item.get("upc")) #if exists, only modify the value by adding the amount
                result[item.get("upc")]= old_value + item.get("unit_price")

    #result = {
    #	'ITEM-453': 131.52,
    #	'ITEM-324': 32.45,
    #	'ITEM-432': 30.08,
    #	'ITEM-23': 8.84,
    #}
    print(result)
    print(f'----------------------------------------------------------------------------------\n')



ejercicio1()
ejercicio2()
ejercicio3()
ejercicio_extra_1()






















