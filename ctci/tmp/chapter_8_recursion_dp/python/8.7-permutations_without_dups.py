def get_perms(string: str):
    """
    Compute all permutations of a string of unique characters.
    """
    if string is None:
        return None
    permutations = []
    if len(string) == 0:  # base case
        permutations.append("")
        return permutations
    first = string[0]
    remainder = string[1:]
    words = get_perms(remainder)
    for word in words:
        for i in range(len(word) + 1):
            s = insert_char_at(word, first, i)
            permutations.append(s)
    return permutations


def insert_char_at(word: str, char: str, index: int):
    """
    Inserts a character at a given position in a string.
    """
    start = "" if not len(word) else word[:index]
    end = "" if not len(word) else word[index:]
    return start + char + end


print(get_perms("abcde"))
"""
[
    'abcde', 'bacde', 'bcade', 'bcdae', 'bcdea', 'acbde', 'cabde',
    'cbade', 'cbdae', 'cbdea', 'acdbe', 'cadbe', 'cdabe', 'cdbae',
    'cdbea', 'acdeb', 'cadeb', 'cdaeb', 'cdeab', 'cdeba', 'abdce',
    'badce', 'bdace', 'bdcae', 'bdcea', 'adbce', 'dabce', 'dbace',
    'dbcae', 'dbcea', 'adcbe', 'dacbe', 'dcabe', 'dcbae', 'dcbea',
    'adceb', 'daceb', 'dcaeb', 'dceab', 'dceba', 'abdec', 'badec',
    'bdaec', 'bdeac', 'bdeca', 'adbec', 'dabec', 'dbaec', 'dbeac',
    'dbeca', 'adebc', 'daebc', 'deabc', 'debac', 'debca', 'adecb',
    'daecb', 'deacb', 'decab', 'decba', 'abced', 'baced', 'bcaed',
    'bcead', 'bceda', 'acbed', 'cabed', 'cbaed', 'cbead', 'cbeda',
    'acebd', 'caebd', 'ceabd', 'cebad', 'cebda', 'acedb', 'caedb',
    'ceadb', 'cedab', 'cedba', 'abecd', 'baecd', 'beacd', 'becad',
    'becda', 'aebcd', 'eabcd', 'ebacd', 'ebcad', 'ebcda', 'aecbd',
    'eacbd', 'ecabd', 'ecbad', 'ecbda', 'aecdb', 'eacdb', 'ecadb',
    'ecdab', 'ecdba', 'abedc', 'baedc', 'beadc', 'bedac', 'bedca',
    'aebdc', 'eabdc', 'ebadc', 'ebdac', 'ebdca', 'aedbc', 'eadbc',
    'edabc', 'edbac', 'edbca', 'aedcb', 'eadcb', 'edacb', 'edcab',
    'edcba'
]
"""
