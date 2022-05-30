/**
 * Determines the number of bits that need to be flipped in order to convert
 * a to b.
 * @param   {number}  a
 * @param   {number}  b
 * @returns {number}
 */
const bit_swap_required = (a, b) => {
  let count = 0
  /* c & (c -1) clears the least significant bit.
   * In this loop, it essentially counts the numbers of 1s. */
  for (let c = a ^ b; c; c = c & (c - 1)) count++
  return count
}

console.log(bit_swap_required(0b11101, 0b01111)) // 2
console.log(bit_swap_required(0b1000001, 0b1111111)) // 5
