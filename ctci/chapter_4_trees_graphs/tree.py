class TreeNode:
    def __init__(self, value: int):
        """
        Tree Node constructor.
        """
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def add_left(self, value: int):
        """
        Adds a node to the left.
        """
        new_node = TreeNode(value)
        new_node.parent = self
        self.left = new_node
        return new_node

    def add_right(self, value: int):
        """
        Adds a node to the right.
        """
        new_node = TreeNode(value)
        new_node.parent = self
        self.right = new_node
        return new_node


def pre_order_traversal(node: TreeNode):
    """
    Prints current node before child nodes.
    """
    if not node:
        return
    print(node.value)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def in_order_traversal(node: TreeNode):
    """
    Prints left nodes, current node, and then right nodes.
    """
    if not node:
        return
    in_order_traversal(node.left)
    print(node.value)
    in_order_traversal(node.right)


def post_order_traversal(node: TreeNode):
    """
    Visits child nodes before current node.
    """
    if not node:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.value)
