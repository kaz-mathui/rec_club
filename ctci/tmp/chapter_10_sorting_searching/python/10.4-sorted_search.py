from typing import List


class Listy:
    def __init__(self):
        """
        Listy constructor.
        """
        self.list = []

    def append(self, val: int):
        """
        Adds a value to Listy's list data structure.
        """
        self.list.append(val)

    def element_at(self, i: int) -> int:
        """
        Returns element at given index or -1 if it does not exist.
        """
        try:
            return self.list[i]
        except IndexError:
            return -1

    def __str__(self):
        """
        String representation.
        """
        return "".join(str(self.list))


def search(listy: Listy, n: int):
    """
    Given a Listy data structure which contains sorted, positive integers,
    finds the index at which an element occurs. If x occurs multiple times,
    returns the first index.
    """
    index = 1
    while listy.element_at(index) != -1 and listy.element_at(index) < n:
        index *= 2
    return binary_search(listy, index // 2, index, n)


def binary_search(listy: Listy, start: int, end: int, n: int) -> int:
    """
    Modified binary search to account for end bound being unknown. Returns
    index of n or -1 if not found.
    """
    while start <= end:
        mid = (start + end) // 2
        mid_val = listy.element_at(mid)
        if mid_val == -1 or mid_val > n:
            end = mid - 1
        elif mid_val < n:
            start = mid + 1
        else:
            return mid
    return -1


l = Listy()
arr = [1, 3, 7, 11, 18, 21, 26, 31, 35, 44, 50]
for i in arr:
    l.append(i)
print(l)
# [1, 3, 7, 11, 18, 21, 26, 31, 35, 44, 50]

print(search(l, 44))  # 9
print(search(l, 3))  # 1
print(search(l, 21))  # 5
print(search(l, 9))  # -1
