def flip_bit(n: int) -> int:
    """
    Calculates number of consecutive 1s if user is able to flip 1 bit to 1.
    """
    prev_len = curr_len = max_len = 0
    while (n):
        if n & 1:
            curr_len += 1
        else:
            prev_len = curr_len if n & 2 else 0
            curr_len = 0
        max_len = max(prev_len + curr_len + 1, max_len)
        n >>= 1
    return max_len


if __name__ == "main":
    print(flip_bit(0b11011101111))  # 8
    print(flip_bit(0b11111101111))  # 11
    print(flip_bit(0b10101010101))  # 3
