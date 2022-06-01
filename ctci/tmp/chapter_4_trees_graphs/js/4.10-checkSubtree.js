const { TreeNode } = require('./tree')

/**
 * Create a string representation of binary with a pre-order traversal.
 * All null attributes are replaced with 'X'.
 * @param   {TreeNode}  root
 * @returns {string}
 */
const getOrderString = root => {
  if (!root) return 'X'
  return root.value + getOrderString(root.left) + getOrderString(root.right)
}

/**
 * Determines if a tree contains another tree.
 * @param   {TreeNode}  firstRoot
 * @param   {TreeNode}  secondRoot
 * @returns {boolean}
 */
const containsTree = (firstRoot, secondRoot) => {
  const str1 = getOrderString(firstRoot)
  const str2 = getOrderString(secondRoot)
  return str1.includes(str2)
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

const m1 = new TreeNode(2)
const m2 = m1.addLeft(4)
const m3 = m1.addRight(5)
const m4 = m2.addLeft(8)
const m5 = m2.addRight(9)
const m6 = m3.addLeft(10)
const m7 = m3.addRight(11)

console.log(containsTree(n1, m1)) // true
m3.right = null
console.log(containsTree(n1, m1)) // false
