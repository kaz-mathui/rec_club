from typing import List


def mfh(arr: List, start: int, end: int) -> int:
    """
    Helper.
    """
    if start > end:
        return -1
    mid_index = (start + end) // 2
    mid_val = arr[mid_index]
    if mid_index == mid_val:
        return mid_index
    # Search left
    left_index = min(mid_index - 1, mid_val)
    left = mfh(arr, 0, left_index)
    if left >= 0:
        return left
    # Search right
    right_index = max(mid_index + 1, mid_val)
    right = mfh(arr, right_index, end)
    return right


def magic_fast(arr: List) -> int:
    """
    Finds the magic index where index == val at index. Values do NOT have to
    be distinct.
    """
    return mfh(arr, 0, len(arr) - 1)


arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(magic_fast(arr))  # 2

arr = [-10, -5, -1, 0, 2, 3, 4, 7, 9, 12, 13]
print(magic_fast(arr))  # 7

arr = [-10, -5, -1, 0, 2, 3, 4, 8, 9, 12, 13]
print(magic_fast(arr))  # -1
