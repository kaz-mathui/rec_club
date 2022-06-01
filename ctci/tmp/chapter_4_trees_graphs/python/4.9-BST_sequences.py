from typing import List
BinarySearchTree = __import__('binary_search_tree').BinarySearchTree
TreeNode = __import__('tree').TreeNode


def all_sequences(root: TreeNode) -> List[List[int]]:
    """
    Finds all possible arrays that could lead to BST.
    """
    result = []
    if not root:
        result.append([])
        return result
    prefix = [root.value]
    # Recurse on left and right subtrees.
    left_seq = all_sequences(root.left)
    right_seq = all_sequences(root.right)
    # Weave together each list from the left and right sides.
    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result.extend(weaved)
    return result


def weave_lists(first: List[int], second: List[int], results: List, prefix: List[int]):
    """
    Weave lists together in all possible ways. This algorithm works by
    removing the head from one list, recursing, and then doing the same
    thing with the other list.
    """
    # One list is empty. Add remainder to [a cloned] prefix and
    # store result.
    if (not len(first) or not len(second)):
        res = prefix[:]
        res.extend(first)
        res.extend(second)
        results.append(res)
        return

    # Recurse with head of first added to the prefix. Removing the head will
    # damage first, so we'll need to put it back where we found it afterwards.
    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)

    # Do the same thing with the second, damaging and then restoring the list.
    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)


if __name__ == "main":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(5)
    bst.insert(15)
    bst.insert(25)

    sequences = all_sequences(bst.root)
    for s in sequences:
        print(s)
    # [ [ 20, 10, 5, 15, 30, 25 ],
    #   [ 20, 10, 5, 30, 15, 25 ],
    #   [ 20, 10, 5, 30, 25, 15 ],
    #   [ 20, 10, 30, 5, 15, 25 ],
    #   [ 20, 10, 30, 5, 25, 15 ],
    #   [ 20, 10, 30, 25, 5, 15 ],
    #   [ 20, 30, 10, 5, 15, 25 ],
    #   [ 20, 30, 10, 5, 25, 15 ],
    #   [ 20, 30, 10, 25, 5, 15 ],
    #   [ 20, 30, 25, 10, 5, 15 ],
    #   [ 20, 10, 15, 5, 30, 25 ],
    #   [ 20, 10, 15, 30, 5, 25 ],
    #   [ 20, 10, 15, 30, 25, 5 ],
    #   [ 20, 10, 30, 15, 5, 25 ],
    #   [ 20, 10, 30, 15, 25, 5 ],
    #   [ 20, 10, 30, 25, 15, 5 ],
    #   [ 20, 30, 10, 15, 5, 25 ],
    #   [ 20, 30, 10, 15, 25, 5 ],
    #   [ 20, 30, 10, 25, 15, 5 ],
    #   [ 20, 30, 25, 10, 15, 5 ] ]
