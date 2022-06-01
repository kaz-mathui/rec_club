# O(n) solution


def string_compression(string: str) -> str:
    """
    Compresses consecutive characters into a number and inserts it into a new
    string along with character.

    String concatentation is slow because of immutability so using a list
    instead.
    """
    _list = []
    count = 1
    for i, e in enumerate(string):
        # if at last index or current and next chars don't match
        if i == len(string) - 1 or string[i] != string[i + 1]:
            _list += [e, str(count)]
            count = 1
        else:
            count += 1
    return ''.join(_list) if len(''.join(_list)) < len(string) else string


if __name__ == '__main__':
    print(string_compression("aaabbc"))  # a3b2c1
    print(string_compression("abc"))  # a1b1c1
    print(string_compression("lliiiinnnuux"))  # l2i4n3u2x1
