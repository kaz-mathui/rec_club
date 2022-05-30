SinglyLinkedList = __import__('singly_linked_list').SinglyLinkedList


class SinglyLinkedList_2_6(SinglyLinkedList):

    def is_palindrome(self) -> bool:
        """
        Determines if a linked list is a palindrome.
        O(n) time and space complexity.
        """
        hare = tortoise = self.head
        stack = []
        # Navigate to middle node.
        while hare and hare.next:
            hare = hare.next.next
            stack.append(tortoise.value)
            tortoise = tortoise.next
        if self.length & 1:
            tortoise = tortoise.next
        while tortoise:
            if tortoise.value != stack.pop():
                return False
            tortoise = tortoise.next
        return True


if __name__ == 'main':
    sll = SinglyLinkedList_2_6()
    arr = [1, 2, 3, 4, 3, 2, 1]
    for i in arr:
        sll.add_to_front(i)
    sll.print_linked_list()  # 1-> 2-> 3-> 4-> 3-> 2-> 1
    print(sll.is_palindrome())  # True

    sll2 = SinglyLinkedList_2_6()
    arr = [1, 2, 3, 3, 2, 1]
    for i in arr:
        sll2.add_to_front(i)
    sll2.print_linked_list()  # 1-> 2-> 3-> 3-> 2-> 1
    print(sll2.is_palindrome())  # True

    sll3 = SinglyLinkedList_2_6()
    arr = [1, 2, 3, 4, 5, 3, 2, 1]
    for i in arr:
        sll3.add_to_front(i)
    sll3.print_linked_list()  # 1-> 2-> 3-> 4-> 5-> 3-> 2-> 1
    print(sll3.is_palindrome())  # False
