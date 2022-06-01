/**
 * Insert m into n at bits i through j.
 * @param   {number}  n
 * @param   {number}  m
 * @param   {number}  i   first index
 * @param   {number}  j   second index
 * @returns {number}
 */
const updateBits = (n, m, i, j) => {
  /* Create a mask to clear bits i through j in n. For simplicity, we'll use
   * 16 bits for the example. */
  const bits = 16
  const allOnes = (1 << (bits + 1)) - 1
  /* 1s before position j, then 0s. */
  const left = allOnes << (j + 1)
  /* 1s after position i. */
  const right = (1 << i) - 1
  const mask = left | right
  /* Clear bits j through i then put m in there. */
  const nCleared = n & mask
  const mShifted = m << i
  return nCleared | mShifted
}

let n = 0b1000000000000000
let m = 0b101

console.log(updateBits(n, m, 2, 4).toString(2))
/* 1000000000010100 */

n = 0b1111111111111111
m = 0b101

console.log(updateBits(n, m, 2, 4).toString(2))
/* 1111111111110111 */
