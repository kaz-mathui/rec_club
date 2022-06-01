from singly_linked_list import SinglyLinkedList

class SinglyLinkedList_4(SinglyLinkedList):

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
                # 先頭に追加
                curr.next = head
                head = curr
            else:
                # 後ろに挿入していくイメージ
                # 今の末尾の次に追加する
                tail.next = curr
                # 末尾をcurrに変える
                tail = curr
            curr = next_node
        tail.next = None
        self.head = head


if __name__ == '__main__':
    sll = SinglyLinkedList_4()
    arr = [10, 30, 11, 31, 12, 33, 13]
    for i in arr:
        sll.add_to_front(i)
    sll.print_linked_list()  # 13 -> 33 -> 12 -> 31 -> 11 -> 30 -> 10
    sll.partition(20)
    sll.print_linked_list()  # 10 -> 11 -> 12 -> 13 -> 33 -> 31 -> 30
