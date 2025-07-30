import os
def clear(): return os.system('clear')


clear()


class Node:
    data: str

    def __init__(self, data, next_left = None, next_right = None):
        self.data = data
        self.next_left = next_left
        self.next_right = next_right


class BinaryTree: 
    def __init__(self, root=Node):
        self.root = root

    def print_structure(self):
        current_node = self.root
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def print_binary_tree(self,node): #visita el nodo padre después de haber visitado sus nodos hijos.
        if node is not None:
            self.print_binary_tree(node.next_left)
            self.print_binary_tree(node.next_right)
            print(node.data, end=' ')


node_1 = Node('A')
node_2 = Node('B')
node_3 = Node('C')
node_4 = Node('D')
node_5 = Node('E')
node_6 = Node('F')
node_7 = Node('G')
node_8 = Node('H')
node_9 = Node('I')
node_10 = Node('J')
node_11 = Node('K')

binaryTree = BinaryTree(node_1)

node_1.next_left = node_2
node_1.next_right = node_3

node_2.next_left = node_4
node_2.next_right = node_5

node_3.next_left = node_6
node_3.next_right = node_7

node_4.next_left = node_8
node_4.next_right = node_9

node_5.next_left = node_10

node_6.next_left = node_11

print('\n\nPost Order')
binaryTree.print_binary_tree(node_1)
print()
