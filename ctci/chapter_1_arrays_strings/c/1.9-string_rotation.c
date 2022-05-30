#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* O(n) solution */

/**
 * Determines if a string is a rotation of another string.
 */
int isRotation(char *str1, char *str2)
{
    int len1, len2, i = 0, j = 0;
    char *str1str1;

    len1 = strlen(str1);
    len2 = strlen(str2);
    if (len1 == len2 && len1)
    {
        str1str1 = malloc((len1 * 2) + 1);
        while (str1[i])
        {
            str1str1[j] = str1[i];
            i++;
            j++;
        }
        i = 0;
        while (str1[i])
        {
            str1str1[j] = str1[i];
            i++;
            j++;
        }
        str1str1[j] = '\0';
        /* Check if str2 is a substring is str1str1. */
        return strstr(str1str1, str2)
                   ? 1
                   : 0;
    }
    return 0;
}

int main(void)
{
    printf("%i\n", isRotation("erbottlewat", "waterbottle")); // 1
    printf("%i\n", isRotation("erbottlewa", "waterbottle"));  // 0
    printf("%i\n", isRotation("bot", "tbo"));                 // 1
    printf("%i\n", isRotation("bot", "tob"));                 // 0

    return 0;
}