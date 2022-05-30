#include <iostream>
#include <string>

/* O(n) solution */

using namespace std;

/**
 * Compresses consecutive characters into a number and inserts it into a new
 * string along with character.
 */
string string_compression(string str)
{
    int count = 1;
    /* In C++, strings are mutable and dynamically sizeable. */
    string result_str = "";

    for (int i = 0; str[i]; i++)
    {
        if (str[i] != str[i + 1])
        {
            result_str += str[i];
            result_str += count + '0';
            count = 1;
        }
        else
            count++;
    }
    return result_str;
}

int main()
{
    cout << string_compression("aaabbc") << endl;       //a3b2c1
    cout << string_compression("abc") << endl;          //a1b1c1
    cout << string_compression("lliiiinnnuux") << endl; //l2i4n3u2x1

    return 0;
}