SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList
Node = __import__('single_linked_list').Node


class SinglyLinkedList_2_7(SinglyLinkedList):

    def intersection(self, other_list: SinglyLinkedList_2_7) -> Node:
        """
        Finds if two linked lists intersect and returns the node where they
        first meet.
        O(n) time and space complexity.
        """
        difference = self.length - other_list.length
        if self.length > other_list.length:
            long = self
            short = other_list
        else:
            long = other_list
            short = self
        long = long.head
        short = short.head
        while difference:
            long = long.next
            difference -= difference
        while long:
            if short == long:
                return short
            long = long.next
            short = short.next
        return None


if __name__ == 'main':
    sll = SinglyLinkedList_2_7()
    sll.add_to_front(1)
    sll.add_to_front(2)
    sll.add_to_front(4)
    n8 = sll.add_to_front(8)
    sll.add_to_front(16)
    sll.add_to_front(32)
    sll.print_linked_list()  # 1-> 2-> 4-> 8-> 16-> 32

    sll2 = SinglyLinkedList_2_7()
    n5 = sll2.add_to_front(5)
    n5.next = n8
    print(sll.intersection(sll2))  # True

    sll3 = SinglyLinkedList_2_7()
    arr = [100, 50, 25, 8, 16, 32]
    for i in arr:
        sll3.add_to_front(i)
    sll3.print_linked_list()  # 32-> 16-> 8-> 25-> 50-> 100
    print(sll.intersection(sll3))  # False
