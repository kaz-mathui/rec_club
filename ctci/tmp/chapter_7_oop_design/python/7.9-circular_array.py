class CircularArray:
    def __init__(self, size: int):
        """
        Circular Array constructor.
        """
        self.items = [0] * size
        self.head = 0
        self.curr = 0

    def convert(self, index: int) -> int:
        """
        Convert index to correct index according to head's position.
        """
        if index < 0:
            index += len(self.items)
        return (self.head + index) % len(self.items)

    def rotate(self, shift_right: int):
        """
        Rotates the head to the right a number of times.
        """
        self.head = self.convert(shift_right)

    def get(self, i: int) -> int:
        """
        Get element at index.
        """
        if i < 0 or i >= len(self.items):
            raise IndexError
        return self.items[self.convert(i)]

    def set(self, index: int, val):
        """
        Set element at index.
        """
        self.items[self.convert(index)] = val

    def __iter__(self):
        """
        Starts iterable.
        """
        self.curr = 0
        return self

    def __next__(self):
        """
        Calls next element in items.
        """
        while self.curr < len(self.items):
            item = self.get(self.curr)
            self.curr += 1
            return item
        raise StopIteration


ca = CircularArray(10)
for i in range(10):
    ca.set(i, i)
for i in ca:
    print(i, end=" ")
print()
# 0 1 2 3 4 5 6 7 8 9
ca.rotate(6)
for i in ca:
    print(i, end=" ")
# 6 7 8 9 0 1 2 3 4 5
