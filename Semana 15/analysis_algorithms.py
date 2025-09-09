#Analice el algoritmo de bubble_sort usando la Big O Notation.
def bubble_ASC(list_of_numbers):
    list_length = len(list_of_numbers)  # O(1)
    for j in range(0, list_length-1):  # O(n)
        any_change = False  # O(1)
        for i in range(0, len(list_of_numbers)-1-j):  # O(n^2)
            current_element = list_of_numbers[i]  # O(1)
            next_element = list_of_numbers[i+1]  # O(1)
            if (current_element > next_element):  # O(1)
                list_of_numbers[i] = next_element  # O(1)
                list_of_numbers[i+1] = current_element  # O(1)
                any_change = True  # O(1)
        if not any_change:  # O(1)
            return list_of_numbers  # O(1)
# R/ el algoritmo de la burbuja tiene una complejidad de O(n^2) 



#Analice los siguientes algoritmos usando la Big O Notation:

#print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list:   # O(n)
		print(number * 2)  # O(1)
# R/ el algoritmo print_numbers_times_2 tiene una complejidad de O(n) 


#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:    # O(n)
		for element_b in list_b:   # O(n^2)
			if element_a == element_b:   # O(1)
				return True  # O(1)
	return False  # O(1)
# R/ el algoritmo check_if_lists_have_an_equal tiene una complejidad de O(n^2) 


#print_10_or_less_elements
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)   # O(1)
	for index in range(min(list_len, 10)):   # O(1)
		print(list_to_print[index])   # O(1)
# R/ el algoritmo print_10_or_less_elements tiene una complejidad de  # O(1)


#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = []   # O(1)
	for element_a in list_a:    # O(n)
		for element_b in list_b:  #O(n^2)
			for element_c in list_c:  #O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')   # O(1)
	return result_list  # O(1)
# R/ el algoritmo generate_list_trios tiene una complejidad de O(n^3)



#⭐ **Ejercicios Extra**
#
#1. Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros `n` números naturales

#- Versión 1:
def manual_add(n):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result


#- Versión 2:
def add_formula(n):
    return number * (number + 1) // 2


# Preguntas:
#- ¿Cuál es la complejidad de cada versión?
    # R/ Para la version 1 su complejidad es de O(n)
    # R/ Para la version 2 su complejidad es de O(1)
    

#- ¿Qué versión usaría si `number = 1 000 000 000`? ¿Por qué?
# R/ usaría la version 2 porque la cantidad de recursos es constante sin importar el tamaño de n






#2. Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False


def binary_search(my_list, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


#- Preguntas:
#    - ¿Cuál es la complejidad de cada algoritmo?
        # R/ la complejidad de linear_search es O(n)
        # R/ la complejidad de binary_search es de O(log(n))

#    - ¿En qué condiciones conviene usar cada uno? 
        # R/ el linear_search conviene usarlo en arrays de un menor tamaño, mientras que el binary_search trabaja de manera mas 
        # eficiente arrays de gran tamaño, y en cada iteracion se descarta la mitad de los elementos sobrantes hasta quedarse con el 
        # elemento buscado


# - ¿Qué pasa si la lista no está ordenada?
# R/ en el caso del linear_search no pasa nada, su complejidad y funcionamiento no cambia ya que en el 
# peor de los casos, deberá pasar por una cantidad n de elementos. Por otra parte en el caso de binary_search, el 
# correcto funcionamiento del algoritmo depende de que la lista esté ordenada, si no lo está, al dividir los bloques de datos, se 
# podría ignorar en el bloque descartado el dato que estamos buscando 



#3. Analice la siguiente función:
def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")


#- Preguntas:
#    - ¿Cuál es la complejidad temporal?
        #R/ la complejidad es de O(n^2)
#    - ¿Cuanto dura si hay `1` millón de claves?
        #R/ Duraría n^2 = 1,000,000^2 de iteraciones































