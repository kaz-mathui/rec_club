/**
 * Returns all subsets of a set.
 * @param   {number[]}  arr
 * @param   {number}    index
 * @returns {number[][]}
 */
const getSubsets = (arr, index) => {
  let allSubsets
  /* Base case, add empty set. */
  if (arr.length === index) allSubsets = [[]]
  else {
    allSubsets = getSubsets(arr, index + 1)
    const item = arr[index]
    const moreSubsets = []
    for (let subset of allSubsets) {
      const newSubset = []
      newSubset.push(...subset)
      newSubset.push(item)
      moreSubsets.push(newSubset)
    }
    allSubsets.push(...moreSubsets)
  }
  return allSubsets
}

const arr = [1, 2, 3, 4, 5]
for (let sub of getSubsets(arr, 0)) console.log(sub)
/*
[]
[ 5 ]
[ 4 ]
[ 5, 4 ]
[ 3 ]
[ 5, 3 ]
[ 4, 3 ]
[ 5, 4, 3 ]
[ 2 ]
[ 5, 2 ]
[ 4, 2 ]
[ 5, 4, 2 ]
[ 3, 2 ]
[ 5, 3, 2 ]
[ 4, 3, 2 ]
[ 5, 4, 3, 2 ]
[ 1 ]
[ 5, 1 ]
[ 4, 1 ]
[ 5, 4, 1 ]
[ 3, 1 ]
[ 5, 3, 1 ]
[ 4, 3, 1 ]
[ 5, 4, 3, 1 ]
[ 2, 1 ]
[ 5, 2, 1 ]
[ 4, 2, 1 ]
[ 5, 4, 2, 1 ]
[ 3, 2, 1 ]
[ 5, 3, 2, 1 ]
[ 4, 3, 2, 1 ]
[ 5, 4, 3, 2, 1 ]
*/
