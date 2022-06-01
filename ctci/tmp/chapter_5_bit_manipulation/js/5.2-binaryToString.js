/**
 * Prints the binary representation of a number between 0 and 1. If number
 * is over 32 digits long, throw error.
 * @param   {number} double
 * @returns {string}
 */
const printBinary = double => {
  str = "0."
  while (double) {
    /* Setting a limit on length: 32 characters. */
    if (str.length > 32) throw new Error()
    const r = double * 2
    if (r >= 1) {
      str += "1"
      double = r - 1
    } else {
      str += "0"
      double = r
    }
  }
  return str
}

console.log(printBinary(0.5)) // 0.1
console.log(printBinary(0.5625)) // 0.1001
