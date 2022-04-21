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

    def node_at_index(self, index):
        if index == 0:
            return self.head
        current = self.head
        position = 0
        while position < index:
            current = current.next_node
            position += 1
        return current

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


def spilt(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half


def merge(left, right):
    merged = LinkedList()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = left.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    head = merged.head.next_node
    merged.head = head
    return merged


def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    left_half, right_half = spilt(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


unsorted_list = LinkedList()

unsorted_list.add(5)
unsorted_list.add(2)
unsorted_list.add(3)
unsorted_list.add(1)
unsorted_list.add(4)
print(unsorted_list)

sorted_list = merge_sort(unsorted_list)
print(sorted_list)
