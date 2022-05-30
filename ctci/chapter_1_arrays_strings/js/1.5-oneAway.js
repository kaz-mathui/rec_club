/* O(n) solution */

/**
 * Compare two strings to determine if they are one edit away from each
 * other.
 * @param   {string}  str1
 * @param   {string}  str2
 * @returns {boolean}
 */
const isOneEditAway = (str1, str2) => {
  const len1 = str1.length
  const len2 = str2.length
  if (len1 === len2) return isOneEditReplace(str1, str2)
  if (Math.abs(len1 - len2) === 1) return isOneEditInsert(str2, str1)
  return false
}

/**
 * Counts the number of differences between two strings of same length.
 * Returns true if the difference is at most one off.
 * @param   {string}  str1
 * @param   {string}  str2
 * @returns {boolean}
 */
const isOneEditReplace = (str1, str2) => {
  let differences = 0
  for (const i in str1) if (str1[i] !== str2[i]) differences++
  return differences <= 1
}

/**
 * Determines shorter string and loops from start to finish. If there is a
 * difference, longer string is adjusted. If there is more than one
 * difference, returns false.
 * @param   {string}  str1
 * @param   {string}  str2
 * @returns {boolean}
 */
const isOneEditInsert = (str1, str2) => {
  const short = str1.length > str2.length ? str2 : str1
  const long = str2.length > str1.length ? str2 : str1
  let foundDifference = false
  for (let i = 0, j = 0; i < short.length; i++, j++) {
    if (short[i] !== long[j]) {
      if (foundDifference) return false
      foundDifference = true
      j++
    }
  }
  return true
}

console.log(isOneEditAway("beal", "bal")) // true
console.log(isOneEditAway("val", "bal")) // true
console.log(isOneEditAway("val", "bale")) // false
console.log(isOneEditAway("mail", "mailman")) // false
console.log(isOneEditAway("abc", "abcde")) // false
console.log(isOneEditAway("abc", "abcd")) // true
