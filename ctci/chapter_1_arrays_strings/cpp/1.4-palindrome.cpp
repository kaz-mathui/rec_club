#include <iostream>
#include <string>
#include <ctype.h>

/* O(n) solution */

using namespace std;

/** 
 * Determines if string or its permutations can be a palindrome.
 */
bool is_pali_permutation(string str)
{
    const int ASCII_LENGTH = 128;
    int map[ASCII_LENGTH] = {0};
    int odds = 0;

    for (auto ch : str)
    {
        if (isalpha(ch))
        {
            map[ch]++;
            map[ch] % 2 != 0
                ? odds++
                : odds--;
        }
    }
    /* Palindrome should have max one odd value at the end of loop. */
    return odds <= 1;
}

int main()
{
    cout << is_pali_permutation("tact coa") << endl;  // 1
    cout << is_pali_permutation("tact coao") << endl; // 1
    cout << is_pali_permutation("tact ccoa") << endl; // 0
    cout << is_pali_permutation("tact coaz") << endl; // 0
    cout << is_pali_permutation("at ta") << endl;     // 1
    cout << is_pali_permutation("t") << endl;         // 1

    return 0;
}