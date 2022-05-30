#include <iostream>
#include <string>
#include <cmath> // for abs()

/* O(n) solution */

using namespace std;

/** 
 * Counts the number of differences between two strings of same length.
 * Returns true if the difference is at most one off.
 */
bool is_one_edit_replace(string str1, string str2)
{
    int differences = 0;

    for (int i = 0; i < str1.length(); i++)
        if (str1[i] != str2[i])
            differences++;
    return differences <= 1;
}

/** 
 * Determines shorter string and loops from start to finish. If there is a
 * difference, longer string is adjusted. If there is more than one
 * difference, returns false.
 */
bool is_one_edit_insert(string str1, string str2)
{
    bool found_difference = false;

    int len1 = str1.length();
    int len2 = str2.length();
    string short_str = (len1 > len2) ? str2 : str1;
    strin long_str = (len1 > len2) ? str1 : str2;
    for (int i = 0, int j = 0; i < short_str.length(); i++, j++)
        if (short_str[i] != long_str[j])
        {
            if (found_difference)
                return false;
            found_difference = true;
            j++;
        }
    return true;
}

/** 
 * Compare two strings to determine if they are one edit away from each other.
 */
bool is_one_edit_away(string str1, string str2)
{
    int len1 = str1.length();
    int len2 = str2.length();
    if (len1 == len2)
        return is_one_edit_replace(str1, str2);
    if (abs(len1 - len2) == 1)
        return is_one_edit_insert(str1, str2);
    return false;
}

int main(void)
{
    cout << is_one_edit_away("beal", "bal") << endl;     // 1
    cout << is_one_edit_away("val", "bal") << endl;      // 1
    cout << is_one_edit_away("val", "bale") << endl;     // 0
    cout << is_one_edit_away("mail", "mailman") << endl; // 0
    cout << is_one_edit_away("abc", "abcde") << endl;    // 0
    cout << is_one_edit_away("", "a") << endl;           // 1

    return 0;
}