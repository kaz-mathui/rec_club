/* O(nlog(n)) solution due to initial sort */

/**
 * Sorts string.
 * @param   {string}  str
 * @returns {string}
 */
const sorted = str =>
  str
    .split("")
    .sort()
    .join("")

/**
 * Determines if two strings are permutations of each other.
 * @param   {string}  str1
 * @param   {string}  str2
 * @returns {boolean}
 */
const checkPermutationSort = (str1, str2) => {
  if (str1.length != str2.length) return false
  return sorted(str1) === sorted(str2)
}

/* O(n) solution */

/**
 * Creates hash table of string.
 * @param   {string}  str
 * @returns {object}
 */
const createMap = str => {
  return str.split("").reduce((a, b) => {
    a[b] ? a[b]++ : (a[b] = 1)
    return a
  }, {})
}

/**
 * Determines if two strings are permutations of each other.
 * @param   {string}  str1
 * @param   {string}  str2
 */
const checkPermutation = (str1, str2) => {
  if (str1.length != str2.length) return false
  const map = createMap(str1)
  for (let ch of str2) {
    if (!map[ch]) return false
    map[ch]--
    /* If array map has a negative value, there is
     * a mismatch in characters. */
    if (map[ch] < 0) return false
  }
  return true
}

console.log(checkPermutation("dog", "god")) // true
console.log(checkPermutation("dog", "God")) // false
console.log(checkPermutation("dog", "good")) // false
console.log(checkPermutation("mmmmm", "mmmmm")) // true
console.log(checkPermutation("mmmmm", "mmmmn")) // false
