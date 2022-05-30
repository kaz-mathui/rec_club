#include <stdio.h>
#include <string.h>

/* O(n) solution */

#define ASCII_LENGTH 128

/**
 * Determines if two strings are permutations of each other.
 */
int check_permutation(char *str1, char *str2)
{
    int len1, len2, i;
    int map[ASCII_LENGTH] = {0};

    len1 = strlen(str1);
    len2 = strlen(str2);
    if (len1 != len2)
        return 0;
    for (i = 0; i < len1; i++)
        /* Map every character to array map. */
        map[str1[i]] += 1;
    for (i = 0; i < len2; i++)
    {
        map[str2[i]]--;
        /* If array map has a negative value, there is a mismatch in
         * characters. */
        if (map[str2[i]] < 0)
            return 0;
    }
    return 1;
}

int main()
{
    printf("%i\n", check_permutation("dog", "god"));     // 1
    printf("%i\n", check_permutation("dog", "God"));     // 0
    printf("%i\n", check_permutation("dog", "good"));    // 0
    printf("%i\n", check_permutation("mmmmm", "mmmmm")); // 1
    printf("%i\n", check_permutation("mmmmm", "mmmmn")); // 0

    return 0;
}