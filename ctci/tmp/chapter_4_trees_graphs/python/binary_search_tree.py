TreeNode = __import__('tree').TreeNode


class BinarySearchTree:
    def __init__(self):
        """
        Binary Search Tree constructor.
        """
        self.root = None
        self.size = 0

    def insert(self, value: int) -> TreeNode:
        """
        Inserts a node into a Binary Search Tree.
        """
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            self.add_node(self.root, node)
        self.size += 1
        return node

    def add_node(self, node: TreeNode, new_node: TreeNode):
        """
        Inserts a node onto another node.
        """
        if new_node.value <= node.value:
            # Insert in left side.
            if not node.left:
                # If left node does not exist, insert.
                node.left = new_node
                new_node.parent = node
            else:
                # Recurse.
                self.add_node(node.left, new_node)
        else:
            # Insert in right side.
            if not node.right:
                # If right node does not exist, insert.
                node.right = new_node
                new_node.parent = node
            else:
                # Recurse.
                self.add_node(node.right, new_node)
