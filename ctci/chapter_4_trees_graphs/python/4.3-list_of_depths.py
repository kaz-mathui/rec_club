from typing import List
SinglyLinkedList = __import__(
    '../../chapter_2_linked_lists/python/singly_linked_list').SinglyLinkedList
TreeNode = __import__('tree').TreeNode


def list_of_depths(root: TreeNode) -> List[SinglyLinkedList]:
    """
    Creates a linked list out of every level in a binary tree.
    """
    res = []
    current = SinglyLinkedList()
    if root:
        current.add_to_front(root)
    while current.length:
        res.append(current)
        tmp = current.head
        current = SinglyLinkedList()
        while tmp:
            # Loop through all nodes in parent.
            if tmp.value.left:
                current.add_to_front(tmp.value.left)
            if tmp.value.right:
                current.add_to_front(tmp.value.right)
            tmp = tmp.next
    return res


def print_linked_list(linked_list: SinglyLinkedList):
    """
    Prints all elements of a singly linked list.
    """
    curr = linked_list.head
    while curr:
        print(curr.value.value, end="-> " if curr.next else "\n")
        curr = curr.next


if __name__ == "main":
    n1 = TreeNode(1)
    n2 = n1.add_left(2)
    n3 = n1.add_right(3)
    n4 = n2.add_left(4)
    n5 = n2.add_right(5)
    n6 = n3.add_left(6)
    n7 = n3.add_right(7)

    res = list_of_depths(n1)
    for linked_list in res:
        print_linked_list(linked_list)
    """
    1
    3-> 2
    5-> 4-> 7-> 6
    """
