from singly_linked_list import SinglyLinkedList
from singly_linked_list import Node

class SinglyLinkedList_8(SinglyLinkedList):
    # Step1 2倍のスピードで動かす
    def find_beginning(self) -> Node:
        """
        Determines if linked list is circular.
        O(n) solution.
        """
        hare = tortoise = self.head
        # 2倍のスピードで動かす
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                break
        if not hare or not hare.next:
            return Node(None)
        tortoise = self.head
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next
        return hare


if __name__ == '__main__':
    sll = SinglyLinkedList_8()
    sll.add_to_front(1)
    n2 = sll.add_to_front(2)
    sll.add_to_front(4)
    sll.add_to_front(8)
    sll.add_to_front(16)
    n32 = sll.add_to_front(32)
    sll.add_to_front(64)
    sll.print_linked_list()  # 64-> 32-> 16-> 8-> 4-> 2-> 1
    sll.find_beginning().print_node()  # False

    # making this circular
    n2.next = n32
    # sll.print_linked_list()
    sll.find_beginning().print_node()  # True
