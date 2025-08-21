import os
def clear(): return os.system('clear')


clear()


# Exercise 1
def bubble_ASC(list_of_numbers):
    generic_number = ""
    for i in range(0, len(list_of_numbers)):
        for j in range(0, len(list_of_numbers)):
            # output = f'[{i}]->{list_of_numbers[i]} [{j}]->{list_of_numbers[j]}'
            if (list_of_numbers[i] < list_of_numbers[j]):
                # output += ' acá hubo cambio'
                generic_number = list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[j]
                list_of_numbers[j] = generic_number
            # print(output)
            # print(list_of_numbers)
    return list_of_numbers

# Exercise 2
def bubble_DESC(list_of_numbers):
    generic_number = ""
    for i in range(len(list_of_numbers)-1, -1, -1):
        for j in range(len(list_of_numbers)-1, -1, -1):
            # output = f'[{i}]->{list_of_numbers[i]} [{j}]->{list_of_numbers[j]}'
            if (list_of_numbers[i] < list_of_numbers[j]):
                # output += ' acá hubo cambio'
                generic_number = list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[j]
                list_of_numbers[j] = generic_number
            # print(output)
            # print(list_of_numbers)
    return list_of_numbers


custom_list = [45, 223, 2, 4, 65, 3, 2, 0, 0, 2, -2, 5]

print('Exercise 1')
result = bubble_ASC(custom_list)
print("ASC -> ", result, '\n')

print('Exercise 2')
result2 = bubble_DESC(custom_list)
print("DES -> ", result2)



print('\nExercise extra 1')


class Node:
    data: int

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self, head=Node):
        self.head = head

    def print_structure(self):
        list_to_print = []
        current_node = self.head
        while (current_node is not None):
            list_to_print.append(current_node.data)
            current_node = current_node.next
        print(list_to_print)
    
    def sortLinkedList(self):
        current_node_i = self.head
        current_node_j = self.head
        generic_number = 0
        while (current_node_i is not None):
            while (current_node_j is not None):
                #print('[i] '+ str(current_node_i.data)+ ' [j] '+ str(current_node_j.data))
                if(current_node_i.data < current_node_j.data):
                    generic_number = current_node_i.data
                    current_node_i.data = current_node_j.data
                    current_node_j.data = generic_number
                current_node_j = current_node_j.next
            current_node_j = self.head
            current_node_i = current_node_i.next


node_1 = Node(67)
node_2 = Node(0)
node_3 = Node(14)
node_4 = Node(17)
node_5 = Node(1)
node_6 = Node(-9)

str_linkedList = linkedList(node_1)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

print('Linked list')
str_linkedList.print_structure()
print('Sorted Linked list')
str_linkedList.sortLinkedList()
str_linkedList.print_structure()

print('\nExercise extra 2')
def bubble_with_changes_and_iterations(list_of_numbers):
    generic_number = ""
    iterations = 0
    changes = 0
    for i in range(0, len(list_of_numbers)):
        for j in range(0, len(list_of_numbers)):
            iterations += 1
            #output = f'[{i}]->{list_of_numbers[i]} [{j}]->{list_of_numbers[j]}'
            if (list_of_numbers[i] < list_of_numbers[j]):
                #output += ' acá hubo cambio'
                generic_number = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[i]
                list_of_numbers[i] = generic_number
                changes += 1
                
            #print(output)
        
    final_print = f'\nLista ordenada: {list_of_numbers}\nIteraciones: {iterations}\nIntercambios: {changes}'
            
    return final_print

custom_list = [34,2,6,1,0,4,4]
print('List: ', custom_list, '\n')
result = bubble_with_changes_and_iterations(custom_list)
print("bubble_with_changes_and_iterations ->",result, '\n')

print('\nExercise extra 3')

def bubble_with_filters(elements_list = []):
    if(len(elements_list) == 0):
        raise IndexError(f'La lista está vacia')
    else:
        for item in elements_list:
            if not isinstance(item, (int, float)) :
                raise ValueError(f'La lista cuenta con elementos no numéricos')
        result = bubble_ASC(elements_list)
    return result

list23 = [1,8,4,9,1,000,-4,"hola"]
list24 = []

try:
    print(bubble_with_filters(list23))
except Exception as ex:
    print(f'An unexpected error occurred: {ex}')
    

try:
    print(bubble_with_filters(list24))
except Exception as ex:
    print(f'An unexpected error occurred: {ex}')
    