from typing import List
TreeNode = __import__('tree').TreeNode
pre_order_traversal = __import__('tree').pre_order_traversal


def create_minimal_bst(arr: List[int]) -> TreeNode:
    """
    Creates a binary search tree with minimal height
    out of sorted array.
    """
    return create_minimal_bst_helper(arr, 0, len(arr) - 1)


def create_minimal_bst_helper(arr: List[int], start: int, end: int) -> TreeNode:
    """
    Helper.
    """
    if start > end:
        return None
    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    node.left = create_minimal_bst_helper(arr, start, mid - 1)
    node.right = create_minimal_bst_helper(arr, mid + 1, end)
    return node


if __name__ == "main":
    arr = [1, 4, 6, 8, 9, 12, 19, 21]
    root = create_minimal_bst(arr)
    pre_order_traversal(root)
    r"""
        8
      /   \
    4       12
    / \     /  \
  1   6   9    19
                /
              21
  """
