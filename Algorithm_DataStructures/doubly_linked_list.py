class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.prev = self.head
            self.head = new_node

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current is not None:
            print(str(current.value) + "->")
            current = current.next

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(str(current.value) + "->")
            current = current.prev

    def peek_front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.value

    def peek_back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.value

    def pop_front(self):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            current.next.prev = None
            self.head = current.next
            current.next = None
            return current.value

    def pop_back(self):
        if self.tail is None:
            print("List is empty")
        else:
            current = self.tail
            current.prev.next = None
            self.tail = current.prev
            current.prev = None
            return current.value

    def insert_after(self, node, value):
        if node == None:
            print("Given node is empty")
        else:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            new_node.prev = node
            if new_node.next is not None:
                new_node.next.prev = new_node
            if node == self.tail:
                self.tail = new_node

    def insert_before(self, node, value):
        if node == None:
            print("Given node is empty")
        else:
            new_node = Node(value)
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        if self.head is node:
            self.head = new_node
