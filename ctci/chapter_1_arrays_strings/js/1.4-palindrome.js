/* O(n) solution */

/**
 * Determines if character is in the alphabet.
 * @param   {string}  ch
 * @returns {boolean}
 */
const isAlpha = ch => {
  /* case insensitive regex */
  return /^[A-Z]$/i.test(ch)
}

/**
 * Determines if string or its permutations can be a palindrome.
 * @param   {string}  str
 * @param   {boolean}
 */
const isPaliPermutation = str => {
  const obj = {}
  let odds = 0
  for (let ch of str) {
    if (isAlpha(ch)) {
      obj[ch] == undefined ? (obj[ch] = 1) : obj[ch]++
      obj[ch] % 2 != 0 ? odds++ : odds--
    }
  }
  /* Palindrome should have max one odd value at the end of loop. */
  return odds <= 1
}

console.log(isPaliPermutation("tact coa")) // true
console.log(isPaliPermutation("tact coao")) // true
console.log(isPaliPermutation("tact ccoa")) // false
console.log(isPaliPermutation("tact coaz")) // false
console.log(isPaliPermutation("at ta")) // true
console.log(isPaliPermutation("t")) // true
