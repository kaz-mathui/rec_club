TreeNode = __import__('tree').TreeNode

# LINK TO PARENTS EXIST


def first_common_ancestor(p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the first common ancestor of two nodes in a binary tree
    if there are links to parents.
    """
    delta = find_depth(p) - find_depth(q)
    if delta > 0:
        first = p
        second = q
    else:
        first = q
        second = p
    first = move_up_by(first, abs(delta))
    while first and second and second != first:
        second = second.parent
        first = first.parent
    if first and second:
        return first
    return None


def move_up_by(node: TreeNode, delta: int) -> TreeNode:
    """
    Moves a node up by a given number of nodes.
    """
    curr = node
    while delta > 0 and curr:
        curr = curr.parent
        delta -= 1
    return curr


def find_depth(node: TreeNode) -> int:
    """
    Finds the depth from a node of a binary tree.
    """
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

# LINK TO PARENTS DOES NOT EXIST


def common_ancestor(root: TreeNode, first: TreeNode, second: TreeNode) -> TreeNode:
    """
    Finds the first common ancestor of two nodes in a binary tree
    if there are no links to parents.
    """
    # Error check - if one node is not in the tree.
    if not covers(root, first) or not covers(root, second):
        return None
    return common_ancestor_helper(root, first, second)


def common_ancestor_helper(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Helper.
    """
    if not root or p == q or q == root:
        return root
    first_on_left = covers(root.left, p)
    second_on_left = covers(root.left, q)
    if first_on_left != second_on_left:
        return root
    child_side = root.left if first_on_left else root.right
    return common_ancestor_helper(child_side, p, q)


def covers(root: TreeNode, node: TreeNode) -> bool:
    """
    Determines if a node has another node in subtree.
    """
    if not root:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


if __name__ == "main":
    n1 = TreeNode(1)
    n2 = n1.add_left(2)
    n3 = n1.add_right(3)
    n4 = n2.add_left(4)
    n5 = n2.add_right(5)
    n6 = n3.add_left(6)
    n7 = n3.add_right(7)
    n8 = n4.add_left(8)
    n9 = n4.add_right(9)
    n10 = n5.add_left(10)
    n11 = n5.add_right(11)
    n12 = n6.add_left(12)
    n13 = n6.add_right(13)
    n15 = TreeNode(15)

    print(first_common_ancestor(n9, n5))  # n2
    print(first_common_ancestor(n9, n15))  # None

    print(common_ancestor(n1, n9, n5))  # n2
    print(common_ancestor(n1, n9, n15))  # None
