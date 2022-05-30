#include <stdio.h>

/* O(n) solution */

/**
 * Counts numbers of spaces in string, given a max bound.
 */
int count_spaces(char *str, int len)
{
    int i, count;

    for (i = 0; i < len; i++)
        if (str[i] == ' ')
            count++;
    return count;
}

/** 
 * Replaces all spaces with "%20". This solution will modify input char array.
 */
void urlify(char str[], int true_length)
{
    int spaces, index, i;

    spaces = count_spaces(str, true_length);
    index = true_length + spaces * 2;
    str[index - 1] = '\0';
    for (i = true_length - 1; i >= 0; i--)
    {
        if (str[i] == ' ')
        {
            str[index - 1] = '0';
            str[index - 2] = '2';
            str[index - 3] = '%';
            index = index - 3;
        }
        else
        {
            str[index - 1] = str[i];
            index--;
        }
    }
}

int main()
{
    char john_smith[] = "Mr John Smith    ";
    printf("[%s]\n", john_smith);
    urlify(john_smith, 13);
    printf("[%s]\n", john_smith);
    /* Mr%20John%20Smith */

    char little_friend[] = "Say hello to my little friend          ";
    printf("[%s]\n", little_friend);
    urlify(little_friend, 29);
    printf("[%s]\n", little_friend);
    /* Say%20hello%20to%20my%20little%20friend */

    return 0;
}