from typing import List
from collections import Counter


def print_perms(string: str) -> List[str]:
    """
    Compute all permutations of a string whoe characters are not necessarily
    unique. The list of permutations should not have duplicates.
    """
    result = []
    counter = Counter(string)
    print_perms_helper(counter, "", len(string), result)
    return result


def print_perms_helper(counter: Counter, prefix: str, remaining: int,
                       result: List):
    """
    Helper.
    """
    # Base case. Permutation has been completed.
    if remaining == 0:
        result.append(prefix)
        return
    # Try remaining letters for next char, and generate remaining permutations.
    for c in counter:
        count = counter[c]
        if count > 0:
            counter[c] -= 1
            print_perms_helper(counter, prefix + c, remaining - 1, result)
            counter[c] = count


print(print_perms("hello"))
"""
[
    'hello', 'helol', 'heoll', 'hlelo', 'hleol', 'hlleo', 'hlloe', 'hloel',
    'hlole', 'hoell', 'holel', 'holle', 'ehllo', 'ehlol', 'eholl', 'elhlo',
    'elhol', 'ellho', 'elloh', 'elohl', 'elolh', 'eohll', 'eolhl', 'eollh',
    'lhelo', 'lheol', 'lhleo', 'lhloe', 'lhoel', 'lhole', 'lehlo', 'lehol',
    'lelho', 'leloh', 'leohl', 'leolh', 'llheo', 'llhoe', 'lleho', 'lleoh',
    'llohe', 'lloeh', 'lohel', 'lohle', 'loehl', 'loelh', 'lolhe', 'loleh',
    'ohell', 'ohlel', 'ohlle', 'oehll', 'oelhl', 'oellh', 'olhel', 'olhle',
    'olehl', 'olelh', 'ollhe', 'olleh'
]
"""
