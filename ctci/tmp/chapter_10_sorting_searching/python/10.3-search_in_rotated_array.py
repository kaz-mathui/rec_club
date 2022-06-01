from typing import List


def search(arr: List, n: int) -> int:
    """
    Given a sorted array of n integers that has been rotated an unknown number
    of times, finds an element in the array. The array is originally sorted
    in increasing order.
    Time complexity is O(log(n)) although worse case can be closer to O(n) if
    the array has a lot of duplicates.
    """
    return search_helper(arr, 0, len(arr) - 1, n)


def search_helper(arr: List, start: int, end: int, n: int) -> int:
    """
    Helper.
    """
    mid = (start + end) // 2
    start_val, mid_val, end_val = arr[start], arr[mid], arr[end]
    if mid_val == n:
        return mid
    if start > end:
        return -1
    # Either the left or right half must be normally ordered. Find out which
    # side is normally ordered, and then use the normally ordered half to
    # figure out which side to search to find n.
    if start_val < mid_val:  # Left is normally ordered.
        if n >= start_val and n < mid_val:
            return search_helper(arr, start, mid - 1, n)
        else:
            return search_helper(arr, mid + 1, end, n)
    elif start_val > mid_val:  # Right is normally ordered.
        if n > mid_val and n <= end_val:
            return search_helper(arr, mid + 1, end, n)
        else:
            return search_helper(arr, start, mid - 1, n)
    # Left or right half is all repeats.
    elif start_val == mid_val:
        # If right is different, search it.
        if mid_val != end_val:
            return search_helper(arr, mid + 1, end, n)
        # Else, we have to search both halves.
        else:
            res = search_helper(arr, start, mid - 1, n)
            if res == -1:
                return search_helper(arr, mid + 1, end, n)
            else:
                return res


arr = [15, 19, 23, 39, 41, 1, 4, 7, 8, 11, 13]
print(search(arr, 23))  # 2
print(search(arr, 15))  # 0
print(search(arr, 1))  # 5
print(search(arr, 11))  # 9
print(search(arr, 13))  # 10
print(search(arr, 99))  # -1

arr = [2, 2, 2, 2, 2, 2, 6, 8, 9, 10, 1, 2]
print(search(arr, 1))  # 10 (almost O(n) runtime)
