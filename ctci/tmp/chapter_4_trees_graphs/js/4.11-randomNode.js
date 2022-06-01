const { TreeNode } = require('./tree')
const { BinarySearchTree } = require('./binarySearchTree')

class TreeNode4_11 extends TreeNode {
  /**
   * TreeNode constructor with size attribute.
   * @param   {number}  value
   */
  constructor(value) {
    super(value)
    this.size = 1
  }

  /**
   * Inserts a node into correct place in Binary Search Tree.
   * @param   {number}  value
   */
  insertInOrder(value) {
    if (value < this.value) {
      if (!this.left) this.left = new TreeNode4_11(value)
      else this.left.insertInOrder(value)
    } else {
      if (!this.right) this.right = new TreeNode4_11(value)
      else this.right.insertInOrder(value)
    }
    this.size++
  }

  /**
   * Retrieves the node at guven index.
   * @param   {number}  index
   * @returns {TreeNode}
   */
  getIthNode(index) {
    const leftSide = this.left == null ? 0 : this.left.size
    if (index < leftSide) return this.left.getIthNode(index)
    else if (index == leftSide) return this
    else return this.right.getIthNode(index - (leftSide + 1))
  }
}

class BinarySearchTree4_11 extends BinarySearchTree {
  /**
   * Inserts a node into correct place in Binary Search Tree.
   * @param   {number}  value
   */
  insertInOrder(value) {
    if (!this.root) this.root = new TreeNode4_11(value)
    else this.root.insertInOrder(value)
    this.size++
  }

  /**
   * Retrieves a random node in Binary Search Tree.
   * @returns {TreeNode}
   */
  getRandomNode() {
    if (!this.root) return null
    /* Get random index */
    const index = Math.floor(Math.random() * this.size)
    return this.root.getIthNode(index)
  }
}

const bst = new BinarySearchTree4_11()
const arr = [20, 30, 10, 15, 35, 17, 5, 3, 7]
arr.forEach(e => bst.insertInOrder(e))
let range = 10
let string = ''
while (range--) string += bst.getRandomNode().value + ' '
console.log(string)
/* 5 10 35 30 7 20 30 17 10 10 */
