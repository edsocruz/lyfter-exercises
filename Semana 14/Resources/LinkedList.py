
import os
def clear(): return os.system('clear')


clear()


class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self, head=Node):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next


node_1 = Node('Primer nodo')
node_2 = Node('Segundo nodo')
node_3 = Node('Tercer Nodo')

str_linkedList = linkedList(node_1)
node_1.next = node_2
node_2.next = node_3

str_linkedList.print_structure()
