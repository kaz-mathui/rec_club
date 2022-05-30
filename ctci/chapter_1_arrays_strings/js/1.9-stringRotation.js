/* O(n) solution */

/**
 * Determines if a string is a rotation of another string.
 * @param   {string}  str1
 * @param   {string}  str2
 * @returns {boolean}
 */
const isRotation = (str1, str2) => {
  if (str1.length == str2.length && str1.length) {
    const str1str1 = str1 + str1
    return str1str1.includes(str2)
  }
  return false
}

console.log(isRotation("erbottlewat", "waterbottle")) // true
console.log(isRotation("erbottlewa", "waterbottle")) // false
console.log(isRotation("bot", "tbo")) // true
console.log(isRotation("bot", "tob")) // false
