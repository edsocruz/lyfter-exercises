import os
def clear(): return os.system('clear')


clear()


class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleEnded_Queue:
    def __init__(self, head=Node):
        self.head = head

        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        self.tail = current_node
        

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node=Node):  # Push Left
        old_head = self.head
        self.head = new_node
        new_node.next = old_head

    def push_right(self, new_node=Node):  # Push right
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = new_node
        self.tail = new_node

    def pop_left(self):  # Pop Left
        if self.head is not None:
            self.head = self.head.next

    def pop_right(self):
        current_node = self.head
        while (current_node.next.next is not None):
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node


node_1 = Node('Primer Nodo')
node_2 = Node('Segundo Nodo')
node_3 = Node('Tercer Nodo')
node_4 = Node('Cuarto Nodo')
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

doubleEnded_Queue = DoubleEnded_Queue(node_1)
print('Constructor test: Head/Tail')
print('Head: ',doubleEnded_Queue.head.data)
print('Tail: ',doubleEnded_Queue.tail.data)
print('\n-----------------')


node_5 = Node('Quinto Nodo')
node_6 = Node('Sexto Nodo')
node_7 = Node('Septimo Nodo')
node_8 = Node('Octavo Nodo')


print('\n\nOriginal List- Push Example')
doubleEnded_Queue.print_structure()

print('\nPush Right')
print('-----------------')
doubleEnded_Queue.push_right(node_5)
doubleEnded_Queue.push_right(node_6)
doubleEnded_Queue.print_structure()
print('-----------------')


print('\nPush Left')
print('-----------------')
doubleEnded_Queue.push_left(node_7)
doubleEnded_Queue.push_left(node_8)
doubleEnded_Queue.print_structure()
print('-----------------')


print('\nAttributes Test')
print('-----------------')
print('Head: ',doubleEnded_Queue.head.data)
print('Tail: ',doubleEnded_Queue.tail.data)
print('-----------------')


print('\n\nOriginal List- Pop Example')
doubleEnded_Queue.print_structure()

print('\n\nPop Left')
print('-----------------')
doubleEnded_Queue.pop_left()
doubleEnded_Queue.pop_left()
doubleEnded_Queue.print_structure()
print('-----------------')

print('\n\nPop Right')
print('-----------------')
doubleEnded_Queue.pop_right()
doubleEnded_Queue.pop_right()
doubleEnded_Queue.print_structure()
print('-----------------')

print('\nAttributes Test')
print('-----------------')
print('Head: ',doubleEnded_Queue.head.data)
print('Tail: ',doubleEnded_Queue.tail.data)
print('-----------------')

