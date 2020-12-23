# STACK 
class Stack():  # FILO
    def __init__(self):
        self.stack = [] 
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size > 0: 
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# QUEUE
class Queue():  # FIFO
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size > 0:
            self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# NODES for LINKED LIST
class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
# LINKED LIST                              head
#                                           \/
class LinkedList(): # singly linked list: [node | pointer] -> [node | pointer] -> None 
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head:
            node.set_next(self.head)
        self.head = node
    
    def print_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.get_next()

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        pass

    def add_to_tail(self, value):
        pass

# BINARY SEARCH TREE
class BinarySearchTree():
    pass
# HASH TABLE

# GRAPH
