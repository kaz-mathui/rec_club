#include <stdio.h>

/* O(n) solution */

#define ASCII_LENGTH 128

/**
 * Determines if an ASCII string has all unique characters.
 */
int is_unique(char *str)
{
    int i, ch;
    int map[ASCII_LENGTH] = {0}; // Array map

    for (i = 0; str[i]; i++)
    {
        ch = str[i];
        if (map[ch] == 1)
            return 0;
        map[ch] = 1;
    }
    return 1;
}

/**
 * Alternate solution. Uses bit vectors, but will only work for a-z chars.
 * O(1) space complexity.
 */
int is_unique_alpha(char *str)
{
    unsigned int bit_map = 0; // 32 bits to works with
    int val, i = 0;

    for (i = 0; str[i]; i++)
    {
        val = str[i] - 'a';
        if ((bit_map & (1 << val)) > 0)
            return 0;
        bit_map |= (1 << val);
    }
    return 1;
}

int main()
{
    printf("%i\n", is_unique("abcdef")); // 1
    printf("%i\n", is_unique("abcdea")); // 0
    printf("%i\n", is_unique("aa"));     // 0
    printf("%i\n", is_unique("a"));      // 1
    printf("%i\n", is_unique("abc123")); // 1
    printf("%i\n", is_unique("abcdef")); // 1

    printf("%i\n", is_unique_alpha("abcdef")); // 1
    printf("%i\n", is_unique_alpha("abcdea")); // 0
    printf("%i\n", is_unique_alpha("aa"));     // 0
    printf("%i\n", is_unique_alpha("a"));      // 1

    return 0;
}