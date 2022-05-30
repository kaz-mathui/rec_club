class FixedMultiStack:
    def __init__(self, stack_size: int):
        """
        Fixed multi-stack constructor.
        """
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values = [0] * stack_size * 3
        # Array of sizes of sub-arrays.
        self.sizes = [0] * 3

    def push(self, stack_num: int, value: int):
        """
        Pushes an element into a given stack.
        """
        if self.is_full(stack_num):
            raise Exception("stack is full")
        self.sizes[stack_num] += 1
        index = self.index_of_top(stack_num)
        self.values[index] = value

    def pop(self, stack_num: int) -> int:
        """
        Pops the top element off a fixed multi-stack.
        """
        if self.is_empty(stack_num):
            raise Exception("stack is empty")
        index = self.index_of_top(stack_num)
        value = self.values[index]
        self.values[index] = 0
        self.sizes[stack_num] -= 1
        return value

    def is_full(self, stack_num: int) -> bool:
        """
        Determines if a fixed multi-stack is full or not.
        """
        return self.sizes[stack_num] == self.stack_capacity

    def is_empty(self, stack_num: int) -> bool:
        """
        Determines if a fixed multi-stack is empty or not.
        """
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num: int) -> int:
        """
        Returns the top index of a given stack.
        """
        offset = stack_num * self.stack_capacity
        index = self.sizes[stack_num]
        return offset + index - 1


if __name__ == "main":
    fms = FixedMultiStack(3)
    print(fms.values)  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(fms.index_of_top(0))  # -1
    print(fms.index_of_top(1))  # 2
    print(fms.index_of_top(2))  # 5
    fms.push(0, 5)
    fms.push(0, 10)
    fms.push(0, 15)
    # fms.push(0, 20) exception
    fms.push(1, 6)
    print(fms.values)  # [5, 10, 15, 6, 0, 0, 0, 0, 0]
    print(fms.is_full(0))  # True
    print(fms.is_empty(1))  # False
    print(fms.is_empty(2))  # True
    print(fms.pop(0))  # 15
    print(fms.values)  # [5, 10, 15, 6, 0, 0, 0, 0, 0]
    print(fms.sizes)  # [2, 1, 0]
    fms.push(0, 25)
    print(fms.values)  # [5, 10, 25, 6, 0, 0, 0, 0, 0]
    # fms.pop(2) exception
