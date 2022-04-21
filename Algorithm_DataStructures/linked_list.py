class Node:
    """
    An object for storing single node of a linked list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data:%s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head:%s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "-> ".join(nodes)

    def is_empty(self):
        return self.head == None

    def size(self):
        """Return the number of nodes in the list"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list,
        Takes O(1) - prepend
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """Searches for the given key in list and returns the postion
        Takes O(n) times
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point
        takes O(n) time
        Overall O(n) time
        """
        if index == 0:
            self.add(data)
            return self.head
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove_at_index():
        return None

    def read_at_index():
        return None

    def remove_key(self, key):

        """Removes Node containing data that matches the key
        Returns the node or None if key doesn't exists
        Takes O(1) for deletion but O(n) for finding the position to be deleted
        """
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current
