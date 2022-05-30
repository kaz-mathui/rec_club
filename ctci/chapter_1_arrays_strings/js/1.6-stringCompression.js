/* O(n) solution */

/**
 * Compresses consecutive characters into a number and inserts it into a new
 * string along with character.
 * @param   {string}  str
 * @returns {string}
 */
const stringCompression = str => {
  /* String concatentation in JS is highly optimized. */
  result_str = ""
  let count = 1
  for (let i = 0; i < str.length; i++) {
    if (str[i] != str[i + 1]) {
      result_str += str[i] + count
      count = 1
    } else count++
  }
  return result_str
}

console.log(stringCompression("aaabbc")) // a3b2c1
console.log(stringCompression("abc")) // a1b1c1
console.log(stringCompression("lliiiinnnuux")) // l2i4n3u2x1
