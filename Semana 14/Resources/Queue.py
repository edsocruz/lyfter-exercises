import os
def clear(): return os.system('clear')


clear()


class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue: #FIFO: First in, first out
    def __init__(self, head=Node):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self, node=Node):
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = node

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.next


node_1 = Node('Primer nodo')
node_2 = Node('Segundo nodo')
node_3 = Node('Tercer Nodo')

queue = Queue(node_1)
node_1.next = node_2
node_2.next = node_3

queue.print_structure()

print('\nDequeue')
queue.dequeue()
queue.print_structure()

print('\nEnqueue')
node_4 = Node('Cuarto nodo')
queue.enqueue(node_4)
queue.print_structure()
