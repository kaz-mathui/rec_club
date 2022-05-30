class TreeNode {
  /**
   * Tree Node constructor.
   * @param   {number}  value
   */
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
    this.parent = null
  }

  /**
   * Adds a node to the left.
   * @param   {number} value
   */
  addLeft(value) {
    const new_node = new TreeNode(value)
    new_node.parent = this
    this.left = new_node
    return new_node
  }
  /**
   * Adds a node to the right.
   * @param   {number} value
   */
  addRight(value) {
    const new_node = new TreeNode(value)
    new_node.parent = this
    this.right = new_node
    return new_node
  }
}

/**
 * Prints current node before child nodes.
 * @param   {TreeNode} node
 */
const preOrderTraversal = node => {
  if (!node) return
  console.log(node.value)
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)
}

/**
 * Prints left nodes, current node, and then right nodes.
 * @param   {TreeNode} node
 */
const inOrderTraversal = node => {
  if (!node) return
  inOrderTraversal(node.left)
  console.log(node.value)
  inOrderTraversal(node.right)
}

/**
 * Visits child nodes before current node.
 * @param   {TreeNode} node
 */
const postOrderTraversal = node => {
  if (!node) return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  console.log(node.value)
}

module.exports = {
  TreeNode,
  preOrderTraversal,
  inOrderTraversal,
  postOrderTraversal
}
