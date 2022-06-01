/**
 * Swap odd and even bits with as few instructions as possible.
 * @param   {number}  n
 * @returns {number}
 */
const swap_odd_even_bits = n => {
  /* 0xaaaaaaaa = 10101010101010101010101010101010 */
  /* 0x55555555 = 01010101010101010101010101010101 */
  const swap_odds = (0xaaaaaaaa & n) >> 1
  const swap_evens = (0x55555555 & n) << 1
  return swap_odds | swap_evens
}

console.log(swap_odd_even_bits(0b11111111).toString(2))
/* 11111111 */
console.log(swap_odd_even_bits(0b10101010).toString(2))
/* 01010101 */
console.log(swap_odd_even_bits(0b11100011).toString(2))
/* 11010011 */
