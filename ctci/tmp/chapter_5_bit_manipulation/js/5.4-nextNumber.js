/**
 * Gets next biggest integer with same amount of 1s in binary representation.
 * @param   {number}  n
 * @returns {number}
 */
const getNext = n => {
  let c = n
  let c0, c1
  c0 = c1 = 0
  while ((c & 1) == 0 && c != 0) {
    c0++
    c >>= 1
  }
  while (c & 1) {
    c1++
    c >>= 1
  }
  /* Position of rightmost non-trailing zero. */
  const p = c0 + c1
  n |= 1 << p // Flip rightmost non-trailing zero.
  n &= ~((1 << p) - 1) // Clear all bits to the right of p.
  n |= (1 << (c1 - 1)) - 1 // Insert (c1 - 1) ones on the right.
  return n
}

console.log(getNext(0b11011001111100).toString(2))
/* 11011010001111 */

/**
 * Get next smallest integer with same amount of 1s in binary representation.
 * @param   {number}  n
 * @returns {number}
 */
const getPrev = n => {
  let c = n
  let c0, c1
  c0 = c1 = 0
  while (c & 1) {
    c1++
    c >>= 1
  }
  if (!c) return -1
  while ((c & 1) == 0 && c) {
    c0++
    c >>= 1
  }
  /* Position of rightmost non-trailing one. */
  p = c0 + c1
  const bits = 16
  /* Clears from bit p onwards. */
  n &= ((1 << (bits + 1)) - 1) << (p + 1)
  /* Sequence of (c1 + 1) ones. */
  n |= ((1 << (c1 + 1)) - 1) << (c0 - 1)
  return n
}

console.log(getPrev(0b10011110000011).toString(2))
/* 10011101110000 */
