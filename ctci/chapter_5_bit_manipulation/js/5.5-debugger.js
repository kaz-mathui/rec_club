/**
 * Determines if a number is a power of two.
 * @param   {number}  n
 * @returns {boolean}
 */
const isPowerOfTwo = n => {
  return n && !(n & (n - 1))
}

console.log(isPowerOfTwo(0)) // false
console.log(isPowerOfTwo(2)) // true
console.log(isPowerOfTwo(6)) // false
console.log(isPowerOfTwo(8)) // true
