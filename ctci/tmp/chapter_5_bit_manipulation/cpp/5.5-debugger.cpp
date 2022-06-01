#include <iostream>

using namespace std;

/**
 * Determines if a number is a power of two.
 */
bool is_power_of_two(unsigned int n)
{
    return n && !(n & (n - 1));
}

int main()
{
    cout << is_power_of_two(0) << endl; // 0
    cout << is_power_of_two(2) << endl; // 1
    cout << is_power_of_two(6) << endl; // 0
    cout << is_power_of_two(8) << endl; // 1

    return 0;
}