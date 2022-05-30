from typing import List


def search(strings: List[str], target: str) -> int:
    """
    Given a sorted array of strings that is interspersed with empty strings,
    finds the location of a given string.
    """
    if len(strings) == 0 or str == "":
        return -1
    return search_helper(strings, target, 0, len(strings) - 1)


def search_helper(strings: List[str], target: str, start: int,
                  end: int) -> int:
    """
    Search helper.
    """
    if start > end:
        return -1
    mid = (start + end) // 2
    if strings[mid] == "":
        left, right = mid - 1, mid + 1
        # Navigate left and right until a valid string is found.
        while True:
            if left < start and right > end:
                return -1
            if left >= start and strings[left] != "":
                mid = left
                break
            elif right <= end and strings[right] != "":
                mid = right
                break
            left -= 1
            right += 1
    if strings[mid] == target:
        return mid
    elif strings[mid] < target:
        return search_helper(strings, target, mid + 1, end)
    else:
        return search_helper(strings, target, start, mid - 1)
    return -1


arr = ["apple", "", "", "ball", "car", "", "", "",
       "delta", "elephant", "", "", "monkey", "", "zebra", ""]
print(search(arr, "monkey"))  # 12
print(search(arr, "zebra"))  # 14
print(search(arr, "apple"))  # 0
print(search(arr, "aardvark"))  # -1
print(search(arr, "car"))  # 4
