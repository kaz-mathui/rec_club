from typing import List


def get_subsets(arr: List, index: int):
    """
    Returns all subsets of a set.
    """
    if len(arr) == index:  # Base case, add empty set.
        all_subsets = [[]]
    else:
        all_subsets = get_subsets(arr, index + 1)
        item = arr[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets.extend(more_subsets)
    return all_subsets


arr = [1, 2, 3, 4, 5]


for sub in get_subsets(arr, 0):
    print(sub)
"""
[][5][4][5, 4]
[3]
[5, 3]
[4, 3]
[5, 4, 3]
[2]
[5, 2]
[4, 2]
[5, 4, 2]
[3, 2]
[5, 3, 2]
[4, 3, 2]
[5, 4, 3, 2]
[1]
[5, 1]
[4, 1]
[5, 4, 1]
[3, 1]
[5, 3, 1]
[4, 3, 1]
[5, 4, 3, 1]
[2, 1]
[5, 2, 1]
[4, 2, 1]
[5, 4, 2, 1]
[3, 2, 1]
[5, 3, 2, 1]
[4, 3, 2, 1]
[5, 4, 3, 2, 1]
"""
