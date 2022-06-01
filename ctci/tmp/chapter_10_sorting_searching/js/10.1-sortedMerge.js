/**
 * Merge two sorted arrays using first array as a buffer.
 * @param   {number[]}  a
 * @param   {number[]}  b
 * @param   {number}    last_a
 * @param   {number}    last_b
 */
const merge = (a, b, last_a, last_b) => {
  let i = last_a + last_b - 1
  last_a--, last_b--
  while (last_b >= 0) {
    if (last_a >= 0 && a[last_a] >= b[last_b]) a[i] = a[last_a--]
    else a[i] = b[last_b--]
    i -= 1
  }
}

const a = [0, 2, 4, 6, 8, 0, 0, 0, 0, 0, 0]
const b = [-1, 1, 3, 6, 9, 12]
merge(a, b, 5, 6)
console.log(a) // [ -1, 0, 1, 2, 3, 4, 6, 6, 8, 9, 12 ]
