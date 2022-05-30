/* O(n) solution */

/**
 * Replaces all spaces with "%20".
 * @param   {string}  str
 * @returns {string}
 */
const urlify = str => {
  return str.trim().replace(/ /g, "%20")
}

console.log(urlify("Mr John Smith    "))
/* Mr%20John%20Smith */
console.log(urlify("Say hello to my little friend          "))
/* Say%20hello%20to%20my%20little%20friend */
