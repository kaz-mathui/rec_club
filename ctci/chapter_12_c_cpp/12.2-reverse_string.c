#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * Reverses a string in place.
 */
void reverse(char *str)
{
    char tmp;
    char *ptr;

    ptr = str;
    while (*ptr)
        ptr++;
    ptr--;
    while (str < ptr)
    {
        tmp = *str;
        *str++ = *ptr;
        *ptr-- = tmp;
    }
}

int main()
{
    char *alphabet = "alphabet";
    char *str;

    str = malloc(sizeof(strlen(alphabet)) * sizeof(char));
    strcpy(str, alphabet);
    reverse(str);
    printf("%s\n", str); // tebahpla
    free(str);
    return 0;
}