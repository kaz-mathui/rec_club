class RankNode:
    def __init__(self, val: int):
        """
        RankNode constructor.
        This node keeps track of how many elements are on the left child of it.
        """
        self.left_side = 0
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val: int):
        """
        Inserts a value to the left or right side of the node.
        """
        if val <= self.val:
            self.left_side += 1
            if self.left:
                return self.left.insert(val)
            else:
                node = RankNode(val)
                self.left = node
                return node
        else:
            if self.right:
                return self.right.insert(val)
            else:
                node = RankNode(val)
                self.right = node
                return node

    def get_rank(self, num: int) -> int:
        """
        Returns the rank of the given number, starting at 0.
        """
        if num == self.val:
            return self.left_side
        if num < self.val:
            if not self.left:
                return -1
            return self.left.get_rank(num)
        else:
            right_side = -1 if not self.right else self.right.get_rank(num)
            if right_side == -1:
                return right_side
            return self.left_side + 1 + right_side


class BinarySearchTree:
    def __init__(self, val: int):
        """
        Binary Search Tree constructor.
        """
        self.root = RankNode(val)

    def track(self, val: int) -> RankNode:
        """
        Inserts a value into the binary search tree.
        """
        return self.root.insert(val)

    def get_rank_of_number(self, num: int) -> int:
        """
        Returns the rank of the given number, starting at 0.
        """
        return self.root.get_rank(num)


root = BinarySearchTree(20)
arr = [15, 10, 13, 5, 25, 23, 24]
for i in arr:
    root.track(i)
print(root.get_rank_of_number(20))  # 4
print(root.get_rank_of_number(5))  # 0
print(root.get_rank_of_number(13))  # 2
print(root.get_rank_of_number(23))  # 5
print(root.get_rank_of_number(24))  # 6
print(root.get_rank_of_number(11))  # -1
print(root.get_rank_of_number(28))  # -1
