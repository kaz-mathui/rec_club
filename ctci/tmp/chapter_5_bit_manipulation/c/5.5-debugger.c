#include <stdio.h>

/**
 * Determines if a number is a power of two.
 */
int is_power_of_two(unsigned int n)
{
    return n && !(n & (n - 1));
}

int main()
{
    printf("%i\n", is_power_of_two(0)); // 0
    printf("%i\n", is_power_of_two(2)); // 1
    printf("%i\n", is_power_of_two(6)); // 0
    printf("%i\n", is_power_of_two(8)); // 1

    return 0;
}