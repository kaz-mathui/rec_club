def bit_swapped_required(a: int, b: int) -> int:
    """
    Determines the number of bits that need to be flipped in order to convert
    a to b.
    """
    count = 0
    c = a ^ b
    while c:
        count += 1
        # c & (c -1) clears the least significant bit.
        # In this loop, it essentially counts the numbers of 1s.
        c = c & (c - 1)
    return count


if __name__ == "main":
    print(bit_swapped_required(0b11101, 0b01111))
    print(bit_swapped_required(0b1000001, 0b1111111))
