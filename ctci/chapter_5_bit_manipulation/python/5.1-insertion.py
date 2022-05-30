def insert_bits(n: int, m: int, i: int, j: int) -> int:
    """
    Insert m into n at bits i through j 
    """
    # Create a mask to clear bits i through j in n. For simplicity, we'll
    # use 16 bits for the example.
    bits = 16
    all_ones = (1 << (bits + 1)) - 1
    # 1s before position j, then 0s.
    left = all_ones << (j + 1)
    # 1s after position i.
    right = (1 << i) - 1
    mask = left | right
    # Clear bits j through i then put m in there.
    n_cleared = mask & n
    m_shifted = m << i
    return n_cleared | m_shifted


if __name__ == "main":
    n = 0b1000000000000000
    m = 0b10101
    print(bin(insert_bits(n, m, 2, 6)))
    # 0b1000000001010100
    print('---')

    n = 0b1111111111111111
    m = 0b10101
    print(bin(insert_bits(n, m, 2, 6)))
    # 0b1111111111010111
