def mph(smaller: int, bigger: int) -> int:
    """
    Helper.
    """
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    half = mph(s, bigger)
    if smaller & 1:
        return (half * 2) + bigger
    return (half * 2)


def min_product(x: int, y: int) -> int:
    """
    Recursively multiple 2 numbers without using * or / operators.
    """
    if x >= y:
        bigger = x
        smaller = y
    else:
        bigger = y
        smaller = x
    return mph(smaller, bigger)


print(min_product(8, 7))  # 56
print(min_product(100, 45))  # 4500
print(min_product(0, 23))  # 0
