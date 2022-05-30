def get_next(n: int) -> int:
    """
    Get next biggest integer with same amount of 1s in binary representation.
    """
    c = n
    c0 = c1 = 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    # Position of rightmost non-trailing zero.
    p = c0 + c1
    n |= (1 << p)  # Flip rightmost non-trailing zero.
    n &= ~((1 << p) - 1)  # Clear all bits to the right of p.
    n |= (1 << (c1 - 1)) - 1  # Insert (c1 - 1) ones on the right.
    return n


def get_prev(n: int) -> int:
    """
    Get next smallest integer with same amount of 1s in binary representation.
    """
    c = n
    c0 = c1 = 0
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    if not c:
        return -1
    while (c & 1) == 0 and c:
        c0 += 1
        c >>= 1
    p = c0 + c1  # Position of rightmost non-trailing one.
    bits = 16
    n &= ((1 << bits + 1) - 1) << (p + 1)  # Clears from bit p onwards.
    n |= (1 << c1 + 1) - 1 << (c0 - 1)  # Sequence of (c1 + 1) ones.
    return n


if __name__ == "main":
    print(bin(get_next(0b11011001111100)))  # b11011010001111
    print(bin(get_prev(0b10011110000011)))  # 0b10011101110000
