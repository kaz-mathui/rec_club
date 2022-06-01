from typing import List


def add_paren(arr: List, left: int, right: int, s: List[str], index: int):
    """
    Adds a parenthesis to an index in a list of characters.
    """
    if left < 0 or right < left:  # Invalid state.
        return
    if left == 0 and right == 0:  # Out of left and right parens.
        arr.append("".join(s))
    else:
        s[index] = '('  # Add left and recurse.
        add_paren(arr, left - 1, right, s, index + 1)
        s[index] = ')'  # Add right and recurse.
        add_paren(arr, left, right - 1, s, index + 1)


def generate_parens(count: int) -> List[str]:
    """
    Prints all valid (properly opened and closed) combinatons of n pairs of
    parentheses.
    """
    s = [0] * (count * 2)
    arr = []
    add_paren(arr, count, count, s, 0)
    return arr


print(generate_parens(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
