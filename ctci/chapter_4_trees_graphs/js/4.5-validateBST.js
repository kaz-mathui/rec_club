const { TreeNode } = require('./tree')

/**
 * Validates that a binary tree is a binary search tree.
 * @param   {TreeNode}  node
 * @returns {boolean}
 */
const validateBST = node => {
  return validateBSTHelper(node, null, null)
}

/**
 * Helper.
 * @param   {TreeNode}  node
 * @param   {number}    min
 * @param   {number}    max
 * @returns {boolean}
 */
const validateBSTHelper = (node, min, max) => {
  if (!node) return true
  if ((min && node.value <= min) || (max && node.value > max)) return false
  if (
    !validateBSTHelper(node.left, min, node.value) ||
    !validateBSTHelper(node.right, node.value, max)
  )
    return false
  return true
}

const n1 = new TreeNode(1)
const n2 = n1.addLeft(2)
const n3 = n1.addRight(3)
const n4 = n2.addLeft(4)
const n5 = n2.addRight(5)
const n6 = n3.addLeft(6)
const n7 = n3.addRight(7)
const n8 = n4.addLeft(8)
const n9 = n4.addRight(9)
const n10 = n5.addLeft(10)
const n11 = n5.addRight(11)
const n12 = n6.addLeft(12)
const n13 = n6.addRight(13)
const n14 = n7.addLeft(14)
const n15 = n7.addRight(15)

const t1 = new TreeNode(20)
const t2 = t1.addLeft(10)
const t3 = t1.addRight(30)
const t4 = t2.addLeft(5)
const t5 = t2.addRight(15)
const t6 = t4.addLeft(3)
const t7 = t4.addRight(7)
const t8 = t5.addRight(17)

console.log(validateBST(n1)) // false
console.log(validateBST(t1)) // true
