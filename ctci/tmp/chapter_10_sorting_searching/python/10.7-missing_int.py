# INT_MAX = 2**31 - 1
# bitfield = [0] * INT_MAX // 8
# If using proper byte array, bitfield can store up 8 billion bits with 1 GB
# of memory. For Python array purposes, we will test with only 512 elements.
bitfield = [0] * 512


def find_open_number(filename: str):
    file = open(filename, "r")
    for line in file:
        n = int(line.strip())
        # Finds the corresponding number in the bitfield by using the OR
        # operator to set the nth bit of a byte (e.g., 10 would correspond
        # to the 2nd bit of index 2 in the byte array).
        bitfield[n // 8] |= 1 << (n % 8)
    for i in range(len(bitfield)):
        for j in range(8):
            # Retrieves the individual bits of each byte. When 0 bit is found,
            # print the corresponding value.
            if bitfield[i] & (1 << j) == 0:
                print(i * 8 + j)
                return


# test.txt has numbers 1-10 on a separate line with the number 7 missing
find_open_number("test.txt")  # 7
