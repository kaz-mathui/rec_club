from typing import List


class Bitset:
    def __init__(self, size: int):
        """
        Bitset constructor.
        """
        self.bitset = [0] * ((size >> 5) + 1)

    def get(self, pos: int) -> bool:
        """
        Determines if bit at given position is equal to one or not.
        """
        word_number = pos >> 5  # Divide by 32.
        bit_number = pos & 0x1F  # Mod by 32.
        return self.bitset[word_number] & (1 << bit_number) != 0

    def set(self, pos: int):
        """
        Sets the bit at given position to one.
        """
        word_number = pos >> 5  # Divide by 32.
        bit_number = pos & 0x1F  # Mod by 32.
        self.bitset[word_number] |= 1 << bit_number


def check_duplicates(arr: List[int]):
    """
    Given an array with all numbers from 1 to N, where N is at most 32000,
    finds the duplicate entries with only 4 kilobytes of memory,
    """
    bs = Bitset(32000)
    for i in range(len(arr)):
        num = arr[i]
        num0 = num - 1  # Bitset starts at 0, numbers start at 1.
        if bs.get(num0):
            print(num)
        else:
            bs.set(num0)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
check_duplicates(arr)  # 2
