# O(n) solution


def is_unique(string: str) -> bool:
    """
    Determines if an ASCII string has all unique characters.
    """
    _dict = {}
    for char in string:
        if char in _dict:
            return False
        _dict[char] = True
    return True


if __name__ == '__main__':
    print(is_unique("abcdef"))  # true
    print(is_unique("abcdea"))  # false
    print(is_unique("aa"))  # false
    print(is_unique("a"))  # true
    print(is_unique("abc123"))  # true
    print(is_unique(""))  # true
