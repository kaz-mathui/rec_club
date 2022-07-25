TreeNode = __import__('tree').TreeNode


def get_order_string(node: TreeNode) -> str:
    """
    Create a string representation of binary with a pre-order traversal. All
    null attributes are replaced with 'X'.
    """
    if not node:
        return "X"
    return str(node.value) + get_order_string(node.left) +\
        get_order_string(node.right)


def contains_tree(first_root: TreeNode, second_root: TreeNode) -> bool:
    """
    Determines if a tree contains another tree.
    """
    str1 = get_order_string(first_root)
    str2 = get_order_string(second_root)
    return str2 in str1


if __name__ == "main":
    n1 = TreeNode(10)
    n2 = n1.add_left(5)
    n3 = n1.add_right(-3)
    n4 = n2.add_left(3)
    n5 = n2.add_right(1)
    n7 = n3.add_right(11)
    n8 = n4.add_left(3)
    n9 = n4.add_right(-2)
    n11 = n5.add_right(2)

    m1 = TreeNode(5)
    m2 = m1.add_left(3)
    m3 = m1.add_right(1)
    m4 = m2.add_left(3)
    m5 = m2.add_right(-2)
    m7 = m3.add_right(2)

    print(contains_tree(n1, m1))  # true
    m3.add_right(0)
    print(contains_tree(n1, m1))  # false
