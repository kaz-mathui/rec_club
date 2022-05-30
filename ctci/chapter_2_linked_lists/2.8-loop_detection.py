SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList


class SinglyLinkedList_2_8(SinglyLinkedList):

    def is_circular(self) -> bool:
        """
        Determines if linked list is circular.
        O(n) solution.
        """
        hare = tortoise = self.head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False


if __name__ == 'main':
    sll = SinglyLinkedList_2_8()
    sll.add_to_front(1)
    n2 = sll.add_to_front(2)
    sll.add_to_front(4)
    sll.add_to_front(8)
    sll.add_to_front(16)
    n32 = sll.add_to_front(32)
    sll.add_to_front(64)
    sll.print_linked_list()  # 64-> 32-> 16-> 8-> 4-> 2-> 1
    print(sll.is_circular())  # False

    # making this circular
    n2.next = n32

    print(sll.is_circular())  # True
