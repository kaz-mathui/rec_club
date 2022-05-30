def print_binary(double: float) -> str:
    """
    Prints the binary representation of a number between 0 and 1. If
    number is over 32 digits long, throw error.
    """
    if double <= 0 or double >= 1:
        raise Exception("Error")
    string = ["0", "."]
    while double:
        # Setting a limit on length: 32 characters.
        if len(string) >= 32:
            raise Exception("Error")
        r = double * 2
        if r >= 1:
            string.append("1")
            double = r - 1
        else:
            string.append("0")
            double = r
    return "".join(string)


if __name__ == "main":
    print(print_binary(0.5))  # 0.1
    print(print_binary(0.5625))  # 0.1001
    print(print_binary(0.70))  # Error
