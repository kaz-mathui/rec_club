# O(n) solution


def is_pali_permutation(string: str) -> bool:
    """
    Determines if string or its permutations can be a palindrome.
    """
    _dict = {}
    odds = 0
    for ch in string:
        if ch.isalpha():
            if ch in _dict:
                _dict[ch] += 1
            else:
                _dict[ch] = 1
            if _dict[ch] % 2 != 0:
                odds += 1
            else:
                odds -= 1
    # Palindrome should have max one odd value at the end of loop.
    return odds <= 1


if __name__ == 'main':
    print(is_pali_permutation("tact coa"))  # true
    print(is_pali_permutation("tact coao"))  # true
    print(is_pali_permutation("tact ccoa"))  # false
    print(is_pali_permutation("tact coaz"))  # false
    print(is_pali_permutation("at ta"))  # true
    print(is_pali_permutation("t"))  # true
