const { TreeNode } = require('./tree')

class BinarySearchTree {
  /**
   * Binary Search Tree constructor.
   */
  constructor() {
    this.root = null
    this.size = 0
  }

  /**
   * Inserts a node into a Binary Search Tree.
   * @param   {number}   value
   * @returns {TreeNode}
   */
  insert(value) {
    const newNode = new TreeNode(value)
    if (!this.root) this.root = newNode
    else this.addNode(this.root, newNode)
    this.size++
    return newNode
  }

  /**
   * Inserts a node onto another node.
   * @param   {TreeNode}  node
   * @param   {TreeNode}  newNode
   */
  addNode(node, newNode) {
    if (newNode.value <= node.value) {
      /* Insert in left side. */
      if (!node.left) {
        /* If left node does not exist, insert. */
        newNode.parent = node
        node.left = newNode
      } else {
        /* Recurse. */
        this.addNode(node.left, newNode)
      }
    } else {
      /* Insert in right side. */
      if (!node.right) {
        /* If right node does not exist, insert. */
        newNode.parent = node
        node.right = newNode
      } else {
        /* Recurse. */
        this.addNode(node.right, newNode)
      }
    }
  }
}

module.exports = {
  BinarySearchTree
}
