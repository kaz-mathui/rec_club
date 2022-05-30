#include <iostream>

using namespace std;

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
    cout << min_prod(8, 7) << endl;    // 56
    cout << min_prod(100, 45) << endl; // 4500
    cout << min_prod(0, 23) << endl;   // 0
    return 0;
}