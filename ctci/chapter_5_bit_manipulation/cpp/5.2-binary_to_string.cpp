#include <iostream>
#include <string>

using namespace std;

/**
 * Prints the binary representation of a number between 0 and 1. If number
 * is over 32 digits long, throw error.
 */
string print_binary(double num)
{
    string s = "0.";

    if (num > 1 || num < 0)
        return "Error";
    while (num)
    {
        /* Setting a limit on length: 32 characters. */
        if (s.length() >= 32)
            return "Error";
        double r = num * 2;
        if (r >= 1)
        {
            s += "1";
            num = r - 1;
        }
        else
        {
            s += "0";
            num = r;
        }
    }
    return s;
}

int main()
{
    cout << print_binary(0.5) << endl;
    /* 0.1 */

    cout << print_binary(0.5625) << endl;
    /* 0.1001 */
    return 0;
}