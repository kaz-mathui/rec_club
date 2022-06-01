from typing import List


def make_change(n: int) -> n:
    """
    Given an infinite number of quarters, dimes, nickels and pennies,
    calculate the number of ways of representing n cents.
    """
    denoms = [25, 10, 5, 1]
    my_map = [[0] * len(denoms) for x in range(n + 1)]
    return make_change_helper(n, denoms, 0, my_map)


def make_change_helper(amount: int, denoms: List[int], index: int,
                       my_map: List[List[int]]) -> int:
    """
    Helper.
    """
    if my_map[amount][index] > 0:  # Retrieve value.
        return my_map[amount][index]
    if index >= len(denoms) - 1:  # One denom remaining.
        return 1
    denom_amount = denoms[index]
    ways = i = 0
    while i * denom_amount <= amount:
        # Go to next denom, assuming i coins of denom amount.
        amount_remaining = amount - (i * denom_amount)
        ways += make_change_helper(amount_remaining, denoms, index + 1, my_map)
        i += 1
    my_map[amount][index] = ways
    return ways


print(make_change(0))  # 1
print(make_change(5))  # 2
print(make_change(10))  # 4
print(make_change(25))  # 13
