# O(n) solution


def urlify(string: str) -> str:
    """
    Replaces all spaces with "%20".
    """
    return string.strip().replace(' ', '%20')


if __name__ == '__main__':
    print(urlify("Mr John Smith    "))
    # Mr%20John%20Smith
    print(urlify("Say hello to my little friend          "))
    # Say%20hello%20to%20my%20little%20friend
