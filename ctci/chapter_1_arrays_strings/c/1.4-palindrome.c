#include <stdio.h>
#include <ctype.h>

/* O(n) solution */

#define ASCII_LENGTH 128

/** 
 * Determines if string or its permutations can be a palindrome.
 */
int is_pali_permutation(char *str)
{
    int map[ASCII_LENGTH] = {0};
    int i, ch, odds = 0;

    for (i = 0; str[i]; i++)
    {
        ch = str[i];
        if (isalpha(ch))
        {
            map[ch]++;
            map[ch] % 2 != 0
                ? odds++
                : odds--;
        }
    }
    /* Palindrome should have max one odd value at the end of loop. */
    return odds <= 1;
}

int main()
{
    printf("%i\n", is_pali_permutation("tact coa"));
    printf("%i\n", is_pali_permutation("tact coao"));
    printf("%i\n", is_pali_permutation("tact ccoa"));
    printf("%i\n", is_pali_permutation("tact coaz"));
    printf("%i\n", is_pali_permutation("at ta"));
    printf("%i\n", is_pali_permutation("t"));

    return 0;
}