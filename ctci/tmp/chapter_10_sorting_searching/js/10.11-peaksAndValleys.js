/**
 * Sorts an array into an alternating sequence of peaks and valleys.
 * @param   {number[]}   arr
 */
const sortValleyPeak = arr => {
  for (let i = 1; i < arr.length; i += 2) {
    const max = findMax(arr, i - 1, i, i + 1)
    if (max !== i) [arr[i], arr[max]] = [arr[max], arr[i]]
  }
}

/**
 * Finds the max value of three given indexes in an array and returns the
 * associated index.
 * @param   {number[]}  arr
 * @param   {number}    prev
 * @param   {number}    curr
 * @param   {number}    next
 * @returns {number}
 */
const findMax = (arr, prev, curr, next) => {
  const a = arr[prev]
  const b = arr[curr]
  const c = next < arr.length ? arr[next] : Number.MIN_SAFE_INTEGER
  const biggest = Math.max(a, b, c)
  if (biggest === a) return prev
  if (biggest === b) return curr
  return next
}

let arr = [9, 1, 0, 4, 8, 7]
sortValleyPeak(arr)
console.log(arr) // [ 1, 9, 0, 8, 4, 7 ]

arr = [-5, -4, 3]
sortValleyPeak(arr)
console.log(arr) // [ -5, 3, -4 ]

arr = [-2]
sortValleyPeak(arr)
console.log(arr) // [ -2 ]

arr = [1, 1, 1]
sortValleyPeak(arr)
console.log(arr) // [ 1, 1, 1 ]
