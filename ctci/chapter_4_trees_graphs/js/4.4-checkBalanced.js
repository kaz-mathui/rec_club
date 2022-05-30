const { TreeNode } = require('./tree')

/**
 * Determines if a binary tree is balanced.
 * @param   {TreeNode}  root
 * @returns {boolean}
 */
const checkBalanced = root => {
  return checkHeight(root) != Number.MIN_VALUE
}

/* Calculates differences between heights of left and right nodes.
 * If difference is greater than 1, return INT_MIN */

/**
 * Calculates differences between heights of left and right nodes.
 * If difference is greater than 1, return INT_MIN.
 * @param   {TreeNode}  root
 * @returns {number}
 */
const checkHeight = root => {
  if (!root) return -1
  let leftHeight = checkHeight(root.left)
  if (leftHeight === Number.MIN_VALUE) return Number.MIN_VALUE
  let rightHeight = checkHeight(root.right)
  if (rightHeight === Number.MIN_VALUE) return Number.MIN_VALUE
  let difference = leftHeight - rightHeight
  if (Math.abs(difference) > 1) return Number.MIN_VALUE
  return Math.max(leftHeight, rightHeight) + 1
}

const n1 = new TreeNode(1)
const n2 = n1.addLeft(2)
const n3 = n1.addRight(3)
const n4 = n2.addLeft(4)
const n5 = n2.addRight(5)
const n6 = n3.addLeft(6)
const n8 = n4.addLeft(8)
const n9 = n4.addRight(9)
const n10 = n5.addLeft(10)
const n11 = n5.addRight(11)
const n12 = n6.addLeft(12)
const n13 = n6.addRight(13)

console.log(checkBalanced(n1)) // false
