/* O(n) solution */

/**
 * Determines if an ASCII string has all unique characters.
 * @param   {string}  str
 * @returns {boolean}
 */
const isUnique = str => {
  const map = {}
  for (let char of str) {
    if (map[char]) return false
    map[char] = true
  }
  return true
}

console.log(isUnique("abcdef")) // true
console.log(isUnique("abcdea")) // false
console.log(isUnique("aa")) // false
console.log(isUnique("a")) // true
console.log(isUnique("abc123")) // true
console.log(isUnique("")) // true
