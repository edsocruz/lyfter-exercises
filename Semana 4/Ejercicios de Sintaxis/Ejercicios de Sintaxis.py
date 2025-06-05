import os
clear = lambda: os.system('clear')
clear()

def ejercicio1():
    #1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    #    1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
    #    Los errores son oportunidades de aprendizaje.
    #    2. Por ejemplo:
    #        1. string + string → ?
    #        2. string + int → ?
    #        3. int + string → ?
    #        4. list + list → ?
    #        5. string + list → ?
    #        6. float + int → ?
    #        7. bool + bool → ?
    #Test data
    name = "Edso"
    age = 25
    favorite_colors =['blue','green','red','white']
    speed= 20.55
    married=False

    print('---------------------------------- Ejercicio #1 ----------------------------------')
    print(f'i. {name+name}')
    #print(f'ii. {name+age}')
    #print(f'iii. {age+name}')
    print(f'iv. {favorite_colors+favorite_colors}')
    #print(f'v. {name+favorite_colors}')
    print(f'vi. {speed+age}')
    print(f'vii. {married+married}')
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio2():
    #Cree un programa que le pida al usuario su 
    #nombre, apellido, y edad, 
    #y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

    print('---------------------------------- Ejercicio #2 ----------------------------------')

    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    age= int(input("Ingrese su edad: "))

    #bebe 0-3
    #niño 4-11
    #preadolecente 12-18
    #adulto joven 18-27
    #adulto 28-59
    #adulto mayor 60 o más

    if(age<=3):
        status = "bebé"
    elif(age<=11):
        status="niño"
    elif(age<=18):
        status = "preadolecente"
    elif(age<=27):
        status="adulto joven"
    elif(age<=59):
        status="adulto"
    elif(age>=60):
        status="adulto mayor"
    print(f'{name} {lastname} usted es un {status}')
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio3():
    #Cree un programa con un numero secreto del 1 al 10. 
    # El programa no debe cerrarse hasta que el usuario adivine el numero.
    print('---------------------------------- Ejercicio #3 ----------------------------------')
    import random
    random_int = random.randint(1, 10)
    print(f'Numero secreto: {random_int}')
    user_number = int(input("Ingrese el valor del número secreto: "))
    while(random_int!=user_number):
        user_number= int(input("¡Incorrecto! Intente de nuevo: "))
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio4():
    #Cree un programa que le pida tres números al usuario y muestre el mayor.
    print('---------------------------------- Ejercicio #4 ----------------------------------')
    user_number=0
    iterator=0
    generic_number=0
    while(iterator<3):
        user_number= int(input(f'Ingrese el valor #{iterator+1}: '))
        if(user_number>generic_number):
            generic_number=user_number
        iterator+=1
    print(f'El número mayor es: {generic_number}')
    print(f'----------------------------------------------------------------------------------\n')

def ejercicio5():
    #5. Dada `n` cantidad de notas de un estudiante, calcular:
        #1. Cuantas notas tiene aprobadas (mayor a 70).
        #2. Cuantas notas tiene desaprobadas (menor a 70).
        #3. El promedio de todas.
        #4. El promedio de las aprobadas.
        #5. El promedio de las desaprobadas.
    print('---------------------------------- Ejercicio #5 ----------------------------------')
    notes_list = [42,58,69,65,70,71,77,80,99,100]
    
    average =0
    average_failed_grades=0
    average_passed_grades=0
    failed_grades=0
    passed_grades=0
    
    print(notes_list)
    
    for grade in notes_list:
        if(grade<70):
            failed_grades +=1
            average_failed_grades = average_failed_grades + grade
        else:
            passed_grades +=1
            average_passed_grades = average_passed_grades + grade
        average= average+grade
        
    average = average / len(notes_list)
    average_passed_grades = average_passed_grades/passed_grades
    average_failed_grades = average_failed_grades/failed_grades
    
    print(f'Notas aprobadas: {passed_grades}')
    print(f'Notas desaprobadas: {failed_grades}')
    print(f'Promedio de las notas aprobadas: {round(average_passed_grades,2)}')
    print(f'Promedio de las notas desaprobadas: {round(average_failed_grades,2)}')
    print(f'Promedio de las notas: {average}')
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_1_1():
    #1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    #    Si el precio es menor a 100, el descuento es del 2%.
    #    Si el precio es mayor o igual a 100, el descuento es del 10%.
    print('---------------Ejercicio extra - 1:  Ejercicios de pseudocódigo 1 ----------------')
    precio_producto = 0
    descuento = 0
    precio_final = 0

    precio_producto = int(input("Introduzca el precio del articulo: $"))

    if(precio_producto < 100 ):
        descuento = precio_producto * 0.02
        precio_final = precio_producto - descuento
    elif(precio_producto >= 100):
        descuento = precio_producto * 0.1
        precio_final = precio_producto - descuento
    print(f"El precio final es: ${precio_final}")
    print('----------------------------------------------------------------------------------\n')
    
def ejercicio_extra_1_2():
    print('---------------Ejercicio extra - 1:  Ejercicios de pseudocódigo 2 ----------------')
    #Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor 
    # o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
    # Si es mayor, muestre “Mayor”.
    
    tiempo_de_comparacion = 600    #60s * 10min =600  
    tiempo_usuario = int(input("Ingrese el tiempo en minutos: "))
    tiempo_usuario = tiempo_usuario*60
    
    if(tiempo_usuario < tiempo_de_comparacion):
        mensaje_final = f'Faltan {tiempo_de_comparacion - tiempo_usuario} segundos para llegar a 10min'
    
    if(tiempo_usuario > tiempo_de_comparacion):
        mensaje_final = "Mayor"
    
    #El escenario en el cual el tiempo_usuario == tiempo_de_comparacion no se especifica en el requerimiento, por tanto queda out of scope
    print(mensaje_final)
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_1_3():
    print('---------------Ejercicio extra - 1:  Ejercicios de pseudocódigo 3 ----------------')
    #Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 
    # 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
    
    iterator = 0
    number_user = int(input("Ingrese el número: "))
    result =0 
    
    while(iterator <= number_user):
        result = result + iterator
        iterator+=1   

    print(f"El resultado final es: {result}" ) 
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_1_4():
    print('------------Ejercicio extra - 1:  Ejercicios extra de pseudocódigo 1 -------------')
    #Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables 
    #distintas (primero y segundo) y los ordene de menor a mayor en dichas variables

    comodin = 0
    primero= int(input(f"Ingrese el primer valor: "))
    segundo= int(input(f"Ingrese el segundo valor: "))

    if(segundo < primero):   
        comodin = segundo     
        segundo = primero     
        primero = comodin     
    
    #si la condicion anterior no se cumple, significa que: el primer valor 
    #es menor que el segundo, por lo tanto ya estarían en el orden correcto 
    #o que ambos valores son el mismo, por tanto es irrelevante su orden 

    print(f"A:  {primero} , B:  {segundo}")
    
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_1_5():
    print('------------Ejercicio extra - 1:  Ejercicios extra de pseudocódigo 2 -------------')
    #Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. 
    #Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos
    
    #1 km == 1000m
    #1 hora == 60 minutos * 60 segundos = 3600s

    velocidad = int(input("Ingrese la velocidad en Kilometros por hora: "))
    metros = velocidad * 1000 / 3600

    print(f"La velocidad es  {round(metros,2)}  m/s")
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_1_6():
    print('------------Ejercicio extra - 1:  Ejercicios extra de pseudocódigo 3 -------------')
    #Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, 
    # ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres
    sexo = 0
    cantidad_personas = 0
    contador_mujeres = 0
    contador_hombres = 0

    print("Ingrese el sexo de las 6 personas, ingresando 1 si es mujer o 2 si es hombre")

    while(cantidad_personas < 6):
        sexo=int(input(f"Igrese el sexo de la persona #{cantidad_personas + 1}: "))
        if(sexo==1):
            contador_mujeres+=1
        elif(sexo==2):
            contador_hombres+=1
        cantidad_personas+=1
    
    print(f"Hay {round(100/6 * contador_mujeres,1)}% mujeres y  {round(100/6 * contador_hombres,1)}% hombres")
    print('----------------------------------------------------------------------------------\n')

#los ejercicios 1 y 2 de diagramas de flujo ya fueron resueltos, brincamos al #3

def ejercicio_extra_2_1():
    print('------------Ejercicio extra - 2: Ejercicios de diagramas de flujo #3 -------------')
#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, 
# o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
    number_1 = int(input("Ingrese el primer valor: "))
    number_2 = int(input("Ingrese el segundo valor: "))
    number_3 = int(input("Ingrese el tercer valor: "))
    if( number_1 == 30 or number_2 == 30 or number_3 == 30 or (number_1 + number_2 + number_3 ==30)):
        print("Correcto")
    else:
        print("Incorrecto")
    print('----------------------------------------------------------------------------------\n')

#El ejercicio extra #1 & #4 de diagramas de flujo es el mismo que el ejercicio #4 (linea 79) solo que en vez de 3 números son 5 y 100 respectivamente
#(Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.)

def ejercicio_extra_2_2():
    print('---Ejercicio extra - 2: Ejercicios de diagramas de flujo, ejercicio extra #2 ----')
#Cree un diagrama de flujo que le pida un numero al usuario y muestre 
#“Fizz” si es divisible entre 3, “Buzz” si es divisible entre 5, y 
#“FizzBuzz” si es divisible entre ambos.
    user_num = int(input("Digite el número a probar: "))
    message=""
    if(user_num%3==0 and user_num%5==0):
        message = "FizzBuzz"
    elif(user_num%3==0):
        message = "Fizz"
    elif(user_num%5==0):
        message = "Buzz"
    print(message)
    print('----------------------------------------------------------------------------------\n')

def ejercicio_extra_2_3():
    print('---Ejercicio extra - 2: Ejercicios de diagramas de flujo, ejercicio extra #3 ----')
    #Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos
    
    iterator = 0
    
    result =0 
    
    while(iterator < 100):
        number_user = int(input(f"Ingrese el valor #{iterator+1}: "))
        result = result + number_user
        iterator+=1   
    print(f"El resultado final es: {result}" ) 
    print('----------------------------------------------------------------------------------\n')


ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio_extra_1_1()
ejercicio_extra_1_2()
ejercicio_extra_1_3()
ejercicio_extra_1_4()
ejercicio_extra_1_5()
ejercicio_extra_1_6()
ejercicio_extra_2_1()
ejercicio_extra_2_2()
ejercicio_extra_2_3()
