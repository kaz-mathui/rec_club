class Node:

    def __init__(self, value: int):
        """
        Node constructor.
        """
        self.value = value
        self.next = None
    
    def print_node(self):
        """
        Prints node.
        """
        curr = self
        while curr:
            print(curr.value, end="-> " if curr.next else "\n")
            curr = curr.next


class SinglyLinkedList:

    def __init__(self):
        """
        Singly linked list constructor.
        """
        self.head = None
        self.length = 0

    def add_to_front(self, value: int) -> Node:
        """
        Adds a new node to the head of a singly linked list.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return node

    def delete_node(self, index: int):
        """
        Deletes a node at a given index.
        """
        curr = self.head
        if index < 0 or index >= self.length:
            raise IndexError
        # Delete head.
        if index == 0:
            self.head = curr.next
            del(curr)
            return
        # Delete last node.
        if index == self.length - 1:
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            del(curr)
            return
        while index != 0 and curr:
            prev = curr
            curr = curr.next
            index -= 1
        prev.next = curr.next
        del(curr)

    def print_linked_list(self):
        """
        Prints all elements of a singly linked list.
        """
        curr = self.head
        while curr:
            print(curr.value, end="-> " if curr.next else "\n")
            curr = curr.next
