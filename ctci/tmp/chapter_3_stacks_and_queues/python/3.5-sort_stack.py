Stack = __import__('stack').Stack


class Stack_3_5(Stack):

    def sort(self):
        """
        Sorts a stack using a secondary stack as a buffer.
        O(n**2) time complexity and O(2n) space complexity.
        """
        buffer = Stack()
        while not self.is_empty():
            tmp = self.pop()
            while not buffer.is_empty() and tmp > buffer.peek():
                # If peeked value in buffer is less than temp,
                # place back in stack.
                self.push(buffer.pop())
            buffer.push(tmp)
        # Place everything in buffer back into stack.
        while not buffer.is_empty():
            self.push(buffer.pop())


if __name__ == "main":
    s = Stack_3_5()
    arr = [3, 6, 2, 7, 9, 4, 1, 5, 8]
    for i in arr:
        s.push(i)
    print(s.stack)
    # [3, 6, 2, 7, 9, 4, 1, 5, 8]
    s.sort()
    print(s.stack)
    # [3, 6, 2, 7, 9, 4, 1, 5, 8]
