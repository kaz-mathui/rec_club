/**
 * Sorts an array of strings so that all anagrams are next to each other.
 * @param   {string[]}  arr
 * @returns {string[]}
 */
const sort_anagrams = arr => {
  const map = {}
  for (let s of arr) {
    const sorted = s
      .split("")
      .sort()
      .join("")
    if (map[sorted] === undefined) map[sorted] = [s]
    else map[sorted].push(s)
  }
  return Object.values(map).reduce((a, b) => {
    a.push(...b)
    return a
  }, [])
}

const arr = ["acre", "home", "race", "hack", "cram", "acer"]
console.log(sort_anagrams(arr))
/* [ 'acre', 'race', 'acer', 'home', 'hack', 'cram' ] */
