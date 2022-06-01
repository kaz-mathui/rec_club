/**
 * Calculates number of consecutive 1s if user if able to flip 1 bit to 1.
 * @param   {number}  n
 * @returns {number}
 */
const flipBits = n => {
  let maxLen = (currLen = prevLen = 0)
  while (n) {
    if (n & 1) currLen++
    else {
      /* Update to 0 (if next bit is 0) or currLen. */
      prevLen = n & 2 ? currLen : 0
      currLen = 0
    }
    maxLen = Math.max(currLen + prevLen + 1, maxLen)
    n >>= 1
  }
  return maxLen
}

console.log(flipBits(0b11011101111)) // 8
console.log(flipBits(0b11111101111)) // 11
console.log(flipBits(0b10101010101)) // 3
