#include <stdio.h>

/**
 * Helper.
 */
int min_prod_helper(int smaller, int bigger)
{
    if (smaller == 0)
        return 0;
    if (smaller == 1)
        return bigger;
    int s = smaller >> 1;
    int half_prod = min_prod_helper(s, bigger);
    if (smaller & 1)
        return (half_prod * 2) + bigger;
    return half_prod * 2;
}

/**
 * Recursively multiple 2 numbers without using * or / operators.
 */
int min_prod(int x, int y)
{
    int bigger = x >= y ? x : y;
    int smaller = x >= y ? y : x;
    return min_prod_helper(smaller, bigger);
}

int main()
{
    printf("%i\n", min_prod(8, 7));    // 56
    printf("%i\n", min_prod(100, 45)); // 4500
    printf("%i\n", min_prod(0, 23));   // 0
    return 0;
}