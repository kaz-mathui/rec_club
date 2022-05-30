#include <iostream>
#include <string.h>
#include <string>

/* O(n) solution */

using namespace std;

/**
 * Determines if a string is a rotation of another string.
 */
bool isRotation(string str1, string str2)
{
    string str1str1 = "";

    if (str1.length() == str2.length() && str1.length())
    {
        str1str1 += str1 + str1;
        /* Have to convert to c strings to use strstr. */
        return strstr(str1str1.c_str(), str2.c_str());
    }
    return 0;
}

int main(void)
{
    cout << isRotation("erbottlewat", "waterbottle") << endl; // 1
    cout << isRotation("erbottlewa", "waterbottle") << endl;  // 0
    cout << isRotation("bot", "tbo") << endl;                 // 1
    cout << isRotation("bot", "tob") << endl;                 // 0

    return 0;
}