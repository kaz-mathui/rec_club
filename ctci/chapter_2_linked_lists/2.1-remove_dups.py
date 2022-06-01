from singly_linked_list import SinglyLinkedList


class SinglyLinkedList_1_1(SinglyLinkedList):
    # バッファを使用する
    def delete_dups(self):
        curr = self.head
        _set = set()
        index = 0
        while curr:
            if curr.value in _set:
                self.delete_node(index)
            else:
                _set.add(curr.value)
                index += 1
            curr = curr.next

class SinglyLinkedList_1_2(SinglyLinkedList):
    # O(n^2)で探索する
    def delete_dups(self):
        curr = self.head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.value == curr.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next


if __name__ == '__main__':
    # sll = SinglyLinkedList_1_1()
    sll = SinglyLinkedList_1_2()
    arr = [2,3,4,4,5,5,10,12,12]
    for i in arr:
        sll.add_to_front(i)
    sll.print_linked_list()
    sll.delete_dups()
    sll.print_linked_list()
