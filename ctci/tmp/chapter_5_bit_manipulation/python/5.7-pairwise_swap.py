def swap_odd_even_bits(n: int) -> int:
    """
    Swap odd and even bits with as few instructions as possible.
    """
    # 0xaaaaaaaa = 10101010101010101010101010101010
    # 0x55555555 = 01010101010101010101010101010101
    swap_odds = (n & 0xaaaaaaaa) >> 1
    swap_evens = (n & 0x55555555) << 1
    return swap_odds | swap_evens


print(bin(swap_odd_even_bits(0b11111111)))  # 0b11111111
print(bin(swap_odd_even_bits(0b10101010)))  # 0b01010101
print(bin(swap_odd_even_bits(0b11100011)))  # 0b11010011
