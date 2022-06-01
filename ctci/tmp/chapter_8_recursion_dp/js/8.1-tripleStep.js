/**
 * Count the possible ways a child can run up the stairs if they can take
 * either 1, 2, or 3 steps at a time.
 * @param   {number} n
 * @param   {object} memo
 * @returns {number}
 */
const count_ways_memo = (n, memo) => {
  let memo = memo || {}
  if (memo[n]) return memo[n]
  if (n < 0) return 0
  if (n === 1) return 1
  memo[n] =
    count_ways_memo(n - 1, memo) +
    count_ways_memo(n - 2, memo) +
    count_ways_memo(n - 3, memo)
  return memo[n]
}

const i = 50
let t0 = new Date().getTime()
console.log(count_ways_memo(i))
let t1 = new Date().getTime()
console.log("Took", (t1 - t0).toFixed(4), "milliseconds to generate.")
/* ~2.0000 */

/**
 * Count the possible ways a child can run up the stairs if they can take
 * either 1, 2, or 3 steps at a time.
 * O(3**n) solution.
 * @param   {number} n
 * @returns {number}
 */
const count_ways = n => {
  if (n < 0) return 0
  if (n === 1) return 1
  return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)
}

t0 = new Date().getTime()
console.log(count_ways(i))
t1 = new Date().getTime()
console.log("Took", (t1 - t0).toFixed(4), "milliseconds to generate.")
/* ~2193.0000 */
