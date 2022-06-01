from typing import List

# O(n**2) solution


def find_pair_bf(arr: List[int], num: int) -> bool:
    """
    Determines if two numbers in a sorted array add up to given number using
    brute force.
    """
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if num - arr[i] == j:
                return True
    return False

# O(nlog(n)) solution


def find_pair_binary_search(arr: List[int], num: int) -> bool:
    """
    Determines if two numbers in a sorted array add up to given number using
    binary search.
    """
    for i in range(len(arr)):
        if binary_search(arr[i + 1:], num - arr[i]):
            return True
    return False


def binary_search(arr: List[int], num: int) -> bool:
    """
    Performs binary search of a number in a sorted array.
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == num:
            return True
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False

# O(n) solution average, best case O(1)


def find_pair_pointers(arr: List[int], num: int) -> bool:
    """
    Determines if two numbers in a sorted array add up to given number using
    two pointers.
    """
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == num:
            return True
        elif arr[start] + arr[end] > num:
            end -= 1
        else:
            start += 1
    return False

# O(n) solution


def find_pair_unsorted(arr: List[int], num: int) -> bool:
    """
    Determines if two numbers in an unsorted array add up to given number
    using a hash table.
    """
    obj = {}
    for i in arr:
        if str(i) in obj:
            return True
        else:
            obj[str(num - i)] = True
    return False


if __name__ == "main":
    ex = [-20, -16, -16, -11, 1, 3, 4, 6, 7, 17]
    print(find_pair_bf(ex, 10))  # True
    print(find_pair_binary_search(ex, 10))  # True
    print(find_pair_pointers(ex, 10))  # True
    print(find_pair_unsorted(ex, 10))  # True
