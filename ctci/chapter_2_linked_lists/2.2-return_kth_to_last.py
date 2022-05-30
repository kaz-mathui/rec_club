SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList
Node = __import__('singly_linked_list').Node


class SinglyLinkedList_2_2(SinglyLinkedList):

    def kth_elem_from_last(self, k: int) -> Node:
        """
        Returns the kth element from last node.
        O(n) time complexity.
        """
        if k < 0 or k > self.length:
            raise IndexError
        curr = kth = self.head
        while k != 0:
            curr = curr.next
            k -= 1
        while curr:
            curr = curr.next
            kth = kth.next
        return kth


if __name__ == 'main':
    sll = SinglyLinkedList_2_2()
    arr = [1, 2, 4, 8, 16, 32]
    for i in arr:
        sll.add_to_front(i)
    sll.print_linked_list()  # 32-> 16-> 8-> 4-> 2-> 1
    node = sll.kth_elem_from_last(1)
    print(node.value)  # 1
    node = sll.kth_elem_from_last(3)
    print(node.value)  # 4
    node = sll.kth_elem_from_last(5)
    print(node.value)  # 16
