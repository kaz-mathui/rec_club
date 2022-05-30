from typing import List


def sort_anagrams(arr: List[str]) -> List[str]:
    """
    Sorts an array of strings so that all anagrams are next to each other.
    """
    hash_table = {}
    for word in arr:
        sorted_word = "".join(sorted(word))
        hash_table.setdefault(sorted_word, []).append(word)
    # List comprehension to flatten list.
    return [v for s in hash_table.values() for v in s]


str_list = ["acre", "home", "race", "hack", "cram", "acer"]
print(sort_anagrams(str_list))
# ['acre', 'race', 'acer', 'home', 'hack', 'cram']
