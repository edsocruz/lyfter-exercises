import os
def clear(): return os.system('clear')


clear()


# Exercise 1
def bubble_ASC(list_of_numbers):
    list_length = len(list_of_numbers)
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
            return list_of_numbers

# Exercise 2
def bubble_DESC(list_of_numbers):
    list_length = len(list_of_numbers)
    for j in range(list_length-1, 0, -1):
        any_change = False
        for i in range(list_length-1, list_length-j-1, -1):
            current_element = list_of_numbers[i]
            previous_element = list_of_numbers[i-1]
            # output = f'[{j}]->{list_of_numbers[i]} [{i+1}]->{list_of_numbers[i+1]}'
            if (current_element > previous_element):
                # output += ' acá hubo cambio'
                list_of_numbers[i] = previous_element
                list_of_numbers[i-1] = current_element
                any_change = True
            # print(output)
        if not any_change:
            break
    return list_of_numbers


custom_list = [1, 9, 0, 2, 8, 3, 7, 4, 6, 5]

print('Exercise 1')
result_ASC = bubble_ASC(custom_list)
print("ASC -> ", result_ASC, '\n')

print('Exercise 2')
result_DESC = bubble_DESC(custom_list)
print("DES -> ", result_DESC)


print('\nExercise extra 1')


class Node:
    data: int

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
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
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            previous = None

            while current is not None and current.next is not None:
                next_node = current.next

                if current.data > next_node.data:
                    # Swap nodes
                    swapped = True
                    if previous is None:
                        # Head is being swapped
                        self.head = next_node
                    else:
                        previous.next = next_node

                    current.next = next_node.next
                    next_node.next = current

                    # Update references
                    previous = next_node
                else:
                    previous = current
                    current = current.next

node_1 = Node(67)
node_2 = Node(0)
node_3 = Node(14)
node_4 = Node(17)
node_5 = Node(1)
node_6 = Node(-9)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6


str_linkedList = LinkedList(node_1)
print('Linked list before sort:')
str_linkedList.print_structure()
str_linkedList.sortLinkedList()
print('Sorted Linked list:')
str_linkedList.print_structure()

print('\nExercise extra 2')
def bubble_with_changes_and_itdderations(list_of_numbers):
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


def bubble_with_changes_and_iterations(list_of_numbers):
    changes = 0
    iterations = 0
    comparisons = 0
    list_length = len(list_of_numbers)
    for j in range(0, list_length-1):
        iterations += 1
        any_change = False
        for i in range(0, len(list_of_numbers)-1-j):
            comparisons+= 1
            current_element = list_of_numbers[i]
            next_element = list_of_numbers[i+1]
            if (current_element > next_element):
                list_of_numbers[i] = next_element
                list_of_numbers[i+1] = current_element
                any_change = True
                changes += 1
        if not any_change:
                final_print = f'\nLista ordenada: {list_of_numbers}\nIteraciones: {iterations}\nIntercambios: {changes}\nComparaciones: {comparisons}'
                return final_print

custom_list = [5,1,2,3,4]

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
    