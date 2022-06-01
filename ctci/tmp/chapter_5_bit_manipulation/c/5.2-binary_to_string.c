#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Prints the binary representation of a number between 0 and 1. If number
 * is over 32 digits long, throw error.
 */
char *print_binary(double num)
{
    char *s;

    s = malloc(sizeof(char) * 32);
    strcat(s, "0.");
    if (num > 1 || num < 0)
        exit(1);
    while (num)
    {
        /* Setting a limit on length: 32 characters. */
        if (strlen(s) >= 32)
        {
            free(s);
            exit(1);
        }
        double r = num * 2;
        if (r >= 1)
        {
            strcat(s, "1");
            num = r - 1;
        }
        else
        {
            strcat(s, "0");
            num = r;
        }
    }
    return s;
}

int main()
{
    char *s;

    s = print_binary(0.5);
    printf("%s\n", s);
    /* 0.1 */
    free(s);

    s = print_binary(0.5625);
    printf("%s\n", s);
    /* 0.1001 */
    free(s);

    printf("%s\n", print_binary(0.70));
    /* error */

    return 0;
}