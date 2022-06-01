const { BinarySearchTree } = require('./bst')
const { TreeNode } = require('./tree')

/**
 * Finds all possible arrays that could lead to BST.
 * @param   {TreeNode}    node
 * @returns {number[][]}
 */
const allSequences = node => {
  const result = []

  if (!node) {
    result.push([])
    return result
  }
  const prefix = []
  prefix.push(node.value)
  /* Recurse on left and right subtrees. */
  const leftSeq = allSequences(node.left)
  const rightSeq = allSequences(node.right)
  /* Weave together each list from the left and right sides. */
  for (let left of leftSeq) {
    for (let right of rightSeq) {
      const weaved = []
      weaveLists(left, right, weaved, prefix)
      result.push(...weaved)
    }
  }
  return result
}

/**
 * Weave lists together in all possible ways. This algorithm works by
 * removing the head from one list, recursing, and then doing the same
 * thing with the other list.
 * @param   {number[]}    first
 * @param   {number[]}    second
 * @param   {number[]}    results
 * @param   {number[]}    prefix
 */
const weaveLists = (first, second, results, prefix) => {
  /* One list is empty. Add remainder to [a cloned] prefix and
   * store result. */
  if (!first.length || !second.length) {
    const result = prefix.slice(0)
    result.push(...first)
    result.push(...second)
    results.push(result)
    return
  }

  /* Recurse with head of first added to the prefix. Removing the head
   * will damage first, so we'll need to put it back where we found it
   * afterwards. */
  let headFirst = first.shift()
  prefix.push(headFirst)
  weaveLists(first, second, results, prefix)
  prefix.pop()
  first.unshift(headFirst)

  /* Do the same thing with the second, damaging and then restoring the
   * list. */
  let headSecond = second.shift()
  prefix.push(headSecond)
  weaveLists(first, second, results, prefix)
  prefix.pop()
  second.unshift(headSecond)
}

bst = new BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.insert(25)

console.log(allSequences(bst.root))
/* 
[ [ 20, 10, 5, 15, 30, 25 ],
  [ 20, 10, 5, 30, 15, 25 ],
  [ 20, 10, 5, 30, 25, 15 ],
  [ 20, 10, 30, 5, 15, 25 ],
  [ 20, 10, 30, 5, 25, 15 ],
  [ 20, 10, 30, 25, 5, 15 ],
  [ 20, 30, 10, 5, 15, 25 ],
  [ 20, 30, 10, 5, 25, 15 ],
  [ 20, 30, 10, 25, 5, 15 ],
  [ 20, 30, 25, 10, 5, 15 ],
  [ 20, 10, 15, 5, 30, 25 ],
  [ 20, 10, 15, 30, 5, 25 ],
  [ 20, 10, 15, 30, 25, 5 ], 
  [ 20, 10, 30, 15, 5, 25 ], 
  [ 20, 10, 30, 15, 25, 5 ],
  [ 20, 10, 30, 25, 15, 5 ],
  [ 20, 30, 10, 15, 5, 25 ],
  [ 20, 30, 10, 15, 25, 5 ],
  [ 20, 30, 10, 25, 15, 5 ],
  [ 20, 30, 25, 10, 15, 5 ] ]
  */
