SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList
Node = __import__('single_linked_list').Node


class SinglyLinkedList_2_3(SinglyLinkedList):

    def del_middle(self, mid_node: Node):
        """
        Deletes a node in the middle of a linked list.
        O(1) time complexity.
        """
        next_node = mid_node.next
        mid_node.value = next_node.value
        mid_node.next = next_node.next
        del(next_node)


if __name__ == 'main':
    sll = SinglyLinkedList_2_3()
    sll.add_to_front(1)
    sll.add_to_front(2)
    node = sll.add_to_front(4)
    sll.add_to_front(8)
    sll.add_to_front(16)

    sll.print_linked_list()  # 16-> 8-> 4-> 2-> 1
    sll.del_middle(node)
    sll.print_linked_list()  # 16-> 8-> 2-> 1
