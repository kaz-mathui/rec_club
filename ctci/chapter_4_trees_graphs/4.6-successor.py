BinarySearchTree = __import__('binary_search_tree').BinarySearchTree
TreeNode = __import__('tree').TreeNode


def left_most_child(node: TreeNode) -> TreeNode:
    """
    Traverse to most left child node.
    """
    while (node.left):
        node = node.left
    return node


def find_successor(node: TreeNode) -> TreeNode:
    """
    Return the next in-order successive node.
    """
    if node.right:
        # If node has right child, traverse down and left.
        return left_most_child(node.right)
    child = node
    parent = child.parent
    # Traverse up to first parent whose left child is not original node or
    # previous parent.
    while (parent and parent.left != child):
        child = parent
        parent = parent.parent
    return parent


if __name__ == "main":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst30 = bst.insert(30)
    bst5 = bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(15)
    bst17 = bst.insert(17)

    print(find_successor(bst5).value)  # 7
    print(find_successor(bst17).value)  # 20
    print(find_successor(bst30))  # None
