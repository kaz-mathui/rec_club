from typing import List

# O(n**3) solution


def max_subarray_cubic(arr: List[int]) -> List[int]:
    """
    Finds maximum subarray within an array.
    """
    start = 0
    end = 0
    max_sum = float("-inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            window = 0
            for k in range(i, j + 1):
                window += arr[k]
            max_sum = max(max_sum, window)
            if max_sum == window:
                start, end = i, j + 1
    return arr[start: end]

# O(n**2) solution


def max_subarray_quadratic(arr: List[int]) -> List[int]:
    """
    Finds maximum subarray within an array.
    """
    start = 0
    end = 0
    max_sum = float("-inf")
    for i in range(len(arr)):
        window = 0
        for j in range(i, len(arr)):
            window += arr[j]
            max_sum = max(max_sum, window)
            if max_sum == window:
                start, end = i, j + 1
    return arr[start: end]

# O(n) solution


def max_subarray_kadane(arr: List[int]) -> List[int]:
    """
    Finds maximum subarray within an array.
    """
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    for i in range(1, len(arr)):
        max_ending_here = max(max_ending_here + arr[i], arr[i])
        if max_ending_here == arr[i]:
            start = i
            end = i
        max_so_far = max(max_so_far, max_ending_here)
        if max_so_far == max_ending_here:
            end = i
    return arr[start: end + 1]

# O(nlog(n)) solution, divide and conquer. Will only return sum, not subarray.


def max_subarray_divide(arr: List[int]) -> List[int]:
    """
    Finds maximum subarray within an array.
    """
    return max_helper(arr, 0, len(arr) - 1)


def max_helper(arr: List[int], l: int, r: int) -> List[int]:
    """
    Helper.
    """
    if (l == r):
        return arr[l]
    m = (l + r) // 2
    return max(max_helper(arr, l, m), max_helper(arr, m + 1, r), max_crossing(arr, l, m, r))


def max_crossing(arr: List[int], l: int, m: int, r: int) -> int:
    """
    Finds max value across an array given left, middle and right indexes.
    """
    _sum = 0
    left_sum = float("-inf")
    for i in range(m, l - 1, -1):
        _sum += arr[i]
        if _sum > left_sum:
            left_sum = _sum
    _sum = 0
    right_sum = float("-inf")
    for i in range(m + 1, r + 1):
        _sum += arr[i]
        if _sum > right_sum:
            right_sum = _sum
    return left_sum + right_sum


if __name__ == "main":
    ex = [4, -1, 10, 6, 9, -5, 3, -8, 0, -2]
    print(max_subarray_cubic(ex))  # [4, -1, 10, 6, 9]
    print(max_subarray_quadratic(ex))  # [4, -1, 10, 6, 9]
    print(max_subarray_kadane(ex))  # [4, -1, 10, 6, 9]
    print(max_subarray_divide(ex))  # 28
