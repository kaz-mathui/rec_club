from typing import List


def merge(a: List, b: List, last_a: int, last_b: int):
    """
    Merges two sorted arrays using first array as a buffer.
    """
    i = last_a + last_b - 1
    last_a -= 1
    last_b -= 1
    while last_b >= 0:
        if last_a >= 0 and a[last_a] >= b[last_b]:
            a[i] = a[last_a]
            last_a -= 1
        else:
            a[i] = b[last_b]
            last_b -= 1
        i -= 1


a = [0, 2, 4, 6, 8, 0, 0, 0, 0, 0, 0]
b = [-1, 1, 3, 6, 9, 12]
merge(a, b, 5, 6)
print(a)  # [-1, 0, 1, 2, 3, 4, 6, 6, 8, 9, 12]
