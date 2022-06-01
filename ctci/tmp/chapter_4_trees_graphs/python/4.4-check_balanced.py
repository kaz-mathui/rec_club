TreeNode = __import__('tree').TreeNode


def check_balanced(root: TreeNode) -> bool:
    """
    Determines if a binary tree is balanced.
    """
    return check_height(root) != float("-inf")


def check_height(root: TreeNode) -> int:
    """
    Calculates differences between heights of left and right nodes.
    If difference is greater than 1, return INT_MIN.
    """
    if root == None:
        return -1
    left_height = check_height(root.left)
    if left_height == float("-inf"):
        return float("-inf")
    right_height = check_height(root.right)
    if right_height == float("-inf"):
        return float("-inf")
    difference = left_height - right_height
    if abs(difference) > 1:
        return float("-inf")
    return max(left_height, right_height) + 1


if __name__ == "main":
    n1 = TreeNode(1)
    n2 = n1.add_left(2)
    n3 = n1.add_right(3)
    n4 = n2.add_left(4)
    n5 = n2.add_right(5)
    n6 = n3.add_left(6)
    # n7 = n3.add_right will make it balanced
    n8 = n4.add_left(8)
    n9 = n4.add_right(9)
    n10 = n5.add_left(10)
    n11 = n5.add_right(11)
    n12 = n6.add_left(12)
    n13 = n6.add_right(13)

    print(check_balanced(n1))  # false
