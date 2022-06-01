/**
 * Finds the magic index where index == val at index. Values do NOT have to
 * be distinct.
 * @param   {number[]}  arr
 * @returns {number}
 */
const magic_fast = arr => {
  return mfh(arr, 0, arr.length - 1)
}

/**
 * Helper func
 * @param   {number[]}  arr
 * @param   {number}    start
 * @param   {number}    end
 * @returns {number}
 */
const mfh = (arr, start, end) => {
  if (start > end) return -1
  const mid_index = Math.floor((start + end) / 2)
  const mid_val = arr[mid_index]
  if (mid_val === mid_index) return mid_index
  /* Search left */
  const left_index = Math.min(mid_index - 1, mid_val)
  const left = mfh(arr, start, left_index)
  if (left >= 0) return left
  /* Search right */
  const right_index = Math.max(mid_index + 1, mid_val)
  const right = mfh(arr, right_index, end)
  return right
}

let arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
console.log(magic_fast(arr)) // 2

arr = [-10, -5, -1, 0, 2, 3, 4, 7, 9, 12, 13]
console.log(magic_fast(arr)) // 7

arr = [-10, -5, -1, 0, 2, 3, 4, 8, 9, 12, 13]
console.log(magic_fast(arr)) // -1
