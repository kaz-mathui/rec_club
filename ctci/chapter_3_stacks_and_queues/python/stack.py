# First in, last out.
class Stack:
    def __init__(self):
        """
        Stack constructor.
        """
        self.stack = []
        self.length = 0

    def push(self, value: int):
        """
        Pushes an element to the top of the stack.
        """
        self.stack.append(value)
        self.length += 1

    def pop(self) -> int:
        """
        Pops an element off the top of the stack.
        """
        self.length -= 1
        return self.stack.pop()

    def peek(self) -> int:
        """
        Peeks at the element at the top of the stack.
        """
        return self.stack[self.length - 1]

    def is_empty(self) -> bool:
        """
        Determines if a stack is empty.
        """
        return self.length == 0


if __name__ == "main":
    s = Stack()
    for i in [1, 2, 3, 4, 5]:
        s.push(i)
    print(s.stack)  # [1, 2, 3, 4, 5]
    print(s.pop())  # 5
    print(s.peek())  # 4
    print(s.stack)  # [1, 2, 3, 4]
