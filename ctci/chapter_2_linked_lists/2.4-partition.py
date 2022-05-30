SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList


class SinglyLinkedList_2_4(SinglyLinkedList):

    def partition(self, number: int):
        """
        Partitions a linked list according to a number. All values lower than
        number will go on the left and all values higher and equal will go on
        the right.
        This solution is unstable, but performs at O(n) time complexity.
        """
        head = tail = curr = self.head
        while curr:
            next_node = curr.next
            if curr.value < number:
                curr.next = head
                head = curr
            else:
                tail.next = curr
                tail = curr
            curr = next_node
        tail.next = None
        self.head = head


if __name__ == 'main':
    sll = SinglyLinkedList_2_4()
    arr = [10, 30, 11, 31, 12, 33, 13]
    for i in arr:
        sll.add_to_front(i)
    sll.print_linked_list()  # 13 -> 33 -> 12 -> 31 -> 11 -> 30 -> 10
    sll.partition(20)
    sll.print_linked_list()  # 10 -> 11 -> 12 -> 13 -> 33 -> 31 -> 30
