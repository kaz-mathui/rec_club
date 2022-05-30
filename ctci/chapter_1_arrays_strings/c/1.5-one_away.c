#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* O(n) solution */

/** 
 * Counts the number of differences between two strings of same length.
 * Returns true if the difference is at most one off.
 */
int is_one_edit_replace(char *str1, char *str2)
{
    int i, differences = 0;

    for (i = 0; i < strlen(str1); i++)
        if (str1[i] != str2[i])
            differences++;
    return differences <= 1;
}

/** 
 * Determines shorter string and loops from start to finish. If there is a
 * difference, longer string is adjusted. If there is more than one
 * difference, returns false.
 */
int is_one_edit_insert(char *str1, char *str2)
{
    char *short_str, *long_str;
    int found_difference = 0, i, j, len1, len2;

    len1 = strlen(str1);
    len2 = strlen(str2);
    short_str = (len1 > len2) ? str2 : str1;
    long_str = (len1 > len2) ? str1 : str2;
    for (i = 0, j = 0; i < strlen(short_str); i++, j++)
        if (short_str[i] != long_str[j])
        {
            if (found_difference)
                return 0;
            found_difference = 1;
            j++;
        }
    return 1;
}

/** 
 * Compare two strings to determine if they are one edit away from each other.
 */
int is_one_edit_away(char *str1, char *str2)
{
    int len1, len2;

    len1 = strlen(str1);
    len2 = strlen(str2);
    if (len1 == len2)
        return is_one_edit_replace(str1, str2);
    if (abs(len1 - len2) == 1)
        return is_one_edit_insert(str1, str2);
    return 0;
}

int main(void)
{
    printf("%i\n", is_one_edit_away("beal", "bal"));     // 1
    printf("%i\n", is_one_edit_away("val", "bal"));      // 1
    printf("%i\n", is_one_edit_away("val", "bale"));     // 0
    printf("%i\n", is_one_edit_away("mail", "mailman")); // 0
    printf("%i\n", is_one_edit_away("abc", "abcde"));    // 0
    printf("%i\n", is_one_edit_away("", "a"));           // 1

    return 0;
}