#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* O(2n) solution 
 * One loop to get size.
 * One loop to place chars in new string. */

/**
 * Returns number of characters needed for final compressed string.
 */
int get_compress_size(char *str)
{
    int i, count = 0;

    for (i = 0; i < str[i]; i++)
        if (str[i] != str[i + 1])
            /* This assumes number is only one digit. */
            count += 2;
    return count;
}

/**
 * Compresses consecutive characters into a number and inserts it into a new
 * string along with character.
 */
char *string_compression(char *str)
{
    int i, count = 1;
    char *result_str, *start;

    result_str = malloc(get_compress_size(str) + 1);
    start = result_str;
    for (i = 0; str[i]; i++)
    {
        if (str[i] != str[i + 1])
        {
            *result_str++ = str[i];
            *result_str++ = count + '0';
            count = 1;
        }
        else
            count++;
    }
    *result_str = '\0';
    return start;
}

int main()
{
    printf("%s\n", string_compression("aaabbc"));       //a3b2c1
    printf("%s\n", string_compression("abc"));          //a1b1c1
    printf("%s\n", string_compression("lliiiinnnuux")); //l2i4n3u2x1
    return 0;
}