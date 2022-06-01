from typing import List


def bubble_down(arr: List[dict], i: int, n: int):
    """
    Bubbles down an element in  a min heap.
    """
    smallest = i
    left = (i * 2) + 1
    right = (i * 2) + 2
    if left < n and arr[left].get("value") < arr[smallest].get("value"):
        smallest = left
    if right < n and arr[right].get("value") < arr[smallest].get("value"):
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        bubble_down(arr, smallest, n)


def heapify(arr: List[dict]):
    """
    Coverts an array into a min heap.
    """
    for i in range(len(arr) - 1, -1, -1):
        bubble_down(arr, i, len(arr))


def merge_k_sorted(arrays: List[List]) -> List:
    """
    Merge a number of sorted arrays in O(k log(k)) time complexity.
    """
    result = []
    min_heap = []
    for i, e in enumerate(arrays):
        min_heap.append({"array_index": i, "element_index": 0, "value": e[0]})
    heapify(min_heap)
    while (min_heap[0].get("value") != float("inf")):
        top = min_heap[0]
        result.append(top.get("value"))
        top["element_index"] += 1
        a_index = top.get("array_index")
        e_index = top.get("element_index")
        if (e_index) >= len(arrays[a_index]):
            top["value"] = float("inf")
        else:
            top["value"] = arrays[a_index][e_index]
        bubble_down(min_heap, 0, len(min_heap))
    return result


arrs = [
    [5, 6,  8,  16, 21],
    [3, 7,  12, 13, 55, 82, 101],
    [1, 10, 11, 15, 16, 22],
    [2, 4,  9,  14, 19],
]

print(merge_k_sorted(arrs))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
# 13, 14, 15, 16, 16, 19, 21, 22, 55, 82, 101]
