/**
 * Recursively multiple 2 numbers without using * or / operators.
 * @param   {number} x
 * @param   {number} y
 * @returns {number}
 */
const minProduct = (x, y) => {
  const smaller = x >= y ? y : x
  const bigger = x >= y ? x : y
  return mph(smaller, bigger)
}

/**
 * Helper.
 * @param   {number} smaller
 * @param   {number} bigger
 * @returns {number}
 */
const mph = (smaller, bigger) => {
  if (smaller === 0) return 0
  if (smaller === 1) return bigger
  const s = smaller >> 1
  const halfProd = mph(s, bigger)
  if (smaller & 1) return halfProd * 2 + bigger
  return halfProd * 2
}

console.log(minProduct(8, 7)) // 56
console.log(minProduct(100, 45)) // 4500
console.log(minProduct(0, 23)) // 0
