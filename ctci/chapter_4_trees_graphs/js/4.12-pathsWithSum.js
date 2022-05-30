const { TreeNode } = require('./tree')

/**
 * Returns the amount of paths in a binary tree that equal a target sum.
 * @param   {TreeNode}  root
 * @param   {number}    targetSum
 * @returns {number}
 */
const countPathsWithSum = (root, targetSum) => {
  return cpwsHelper(root, targetSum, 0, {})
}

/**
 * Helper.
 * @param   {TreeNode}  node
 * @param   {number}    targetSum
 * @param   {number}    runningSum
 * @param   {Object}    pathCount
 * @returns {number}
 */
const cpwsHelper = (node, targetSum, runningSum, pathCount) => {
  if (!node) return 0
  /* Count paths with sum ending at the current node */
  runningSum += node.value
  const sum = runningSum - targetSum
  let totalPaths = pathCount[sum] || 0
  /* If runningSum equals targetSum, then one additional path starts at root.
   * Add in this path. */
  if (runningSum == targetSum) {
    totalPaths++
  }

  /* Increment pathCount, recurse, then decrement pathCount. */
  modifyHashTable(pathCount, runningSum, 1) // Increment pathCount
  totalPaths += cpwsHelper(node.left, targetSum, runningSum, pathCount)
  totalPaths += cpwsHelper(node.right, targetSum, runningSum, pathCount)
  modifyHashTable(pathCount, runningSum, -1) // Decrement pathCount
  return totalPaths
}

/**
 * Modifies a key in a hash table
 * @param   {Object}    hashTable
 * @param   {string}    key
 * @param   {number}    delta
 */
const modifyHashTable = (hashTable, key, delta) => {
  const newCount = (hashTable[key] || 0) + delta
  if (!newCount)
    /* Remove when zero to reduce space usage. */
    delete hashTable[key]
  else hashTable[key] = newCount
}

const n1 = new TreeNode(10)
const n2 = n1.addLeft(5)
const n3 = n1.addRight(-3)
const n4 = n2.addLeft(3)
const n5 = n2.addRigh(1)
const n7 = n3.addRight(11)
const n8 = n4.addLeft(3)
const n9 = n4.addRight(-2)
const n11 = n5.addRight(2)

console.log(countPathsWithSum(n1, 8)) // 3
