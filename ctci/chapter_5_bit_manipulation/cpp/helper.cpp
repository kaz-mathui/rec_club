#include <iostream>

using namespace std;

/**
 * Prints the binary presentation of an integer.
 */
void bin(int n)
{
    bool flag = false;
    /* Size of an integer is assumed to be 32 bits. */
    for (int i = 31; i >= 0; i--)
    {
        int k = n >> i;
        if (k & 1)
        {
            cout << "1";
            flag = true;
        }
        else if (flag)
            cout << "0";
    }
    cout << endl;
}