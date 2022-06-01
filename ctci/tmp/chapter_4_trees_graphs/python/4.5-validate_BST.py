TreeNode = __import__('tree').TreeNode


def validate_bst_helper(root: TreeNode, minimum: int, maximum: int) -> bool:
    """
    Helper.
    """
    if not root:
        return True
    if (minimum and root.value < minimum) or (maximum and root.value > maximum):
        return False
    if not validate_bst_helper(root.left, minimum, root.value) or \
       not validate_bst_helper(root.right, root.value, maximum):
        return False
    return True


def validate_bst(root: TreeNode) -> bool:
    """
    Validates that a binary tree is a binary search tree.
    """
    return validate_bst_helper(root, None, None)


if __name__ == "main":
    n1 = TreeNode(15)
    n2 = n1.add_left(12)
    n3 = n1.add_right(22)
    n4 = n2.add_left(11)
    n5 = n2.add_right(14)
    n6 = n3.add_left(16)
    n7 = n4.add_right(30)
    # n3.add_right(17) # False

    print(validate_bst(n1))  # True
