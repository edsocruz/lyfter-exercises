import os
def clear(): return os.system('clear')


clear()


class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack: #LIFO: Last in, first out
    def __init__(self, head=Node):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node = Node):
        old_head = self.head
        self.head = new_node
        new_node.next = old_head
        

    def pop(self):
        if self.head is not None:
            self.head = self.head.next


node_1 = Node('Primer nodo')
node_2 = Node('Segundo nodo')
node_3 = Node('Tercer Nodo')

stack = Stack(node_1)

print('Push')
stack.print_structure()
stack.push(node_2)
print('\n-----------------')
stack.print_structure()
stack.push(node_3)
print('\n-----------------')
stack.print_structure()


print('\n\nPop')
stack.print_structure()
stack.pop()
print('\n-----------------')
stack.print_structure()
stack.pop()
print('\n-----------------')
stack.print_structure()

