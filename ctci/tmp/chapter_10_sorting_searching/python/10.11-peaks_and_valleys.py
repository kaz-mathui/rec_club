from typing import List


def sort_valley_peak(arr: List):
    """
    Sorts an array into an alternating sequence of peaks and valleys.
    """
    for i in range(1, len(arr), 2):
        m = find_max(arr, i - 1, i, i + 1)
        if i != m:
            arr[i], arr[m] = arr[m], arr[i]


def find_max(arr: List, prev: int, curr: int, next: int) -> int:
    """
    Finds the max value of three given indexes in an array and returns the
    associated index.
    """
    a, b = arr[prev], arr[curr]
    c = arr[next] if next < len(arr) else float("-inf")
    biggest = max(a, b, c)
    if a == biggest:
        return prev
    if b == biggest:
        return curr
    return next


arr = [9, 1, 0, 4, 8, 7]
sort_valley_peak(arr)
print(arr)  # [1, 9, 0, 8, 4, 7

arr = [-5, -4, 3]
sort_valley_peak(arr)
print(arr)  # [-5, 3, -4]

arr = [-2]
sort_valley_peak(arr)
print(arr)  # [-2]

arr = [1, 1, 1]
sort_valley_peak(arr)
print(arr)  # [1, 1, 1]
