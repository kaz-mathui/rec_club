# O(n) solution


def is_rotation(str1: str, str2: str) -> bool:
    """
    Determines if a string is a rotation of another string.
    """
    if len(str1) == len(str2) and len(str1):
        str1str1 = str1 * 2
        return str2 in str1str1
    return False


if __name__ == "__main__":
    print(is_rotation("erbottlewat", "waterbottle"))  # true
    print(is_rotation("erbottlewa", "waterbottle"))  # false
    print(is_rotation("bot", "tbo"))  # true
    print(is_rotation("bot", "tob"))  # false
