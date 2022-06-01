#include <iostream>
#include <vector>

using namespace std;

/**
 * Merge two sorted arrays using first array as a buffer.
 */
void merge(vector<int> &a, vector<int> &b, int last_a, int last_b)
{
    int i = last_a + last_b - 1;
    last_a--;
    last_b--;
    while (last_b >= 0)
    {
        a[i] = (last_a >= 0 && a[last_a] >= b[last_b])
                   ? a[last_a--]
                   : b[last_b--];
        i--;
    }
}

int main()
{
    vector<int> a{0, 2, 4, 6, 8, 0, 0, 0, 0, 0, 0};
    vector<int> b{-1, 1, 3, 6, 9, 12};
    merge(a, b, 5, 6);
    for (auto i : a)
        cout << i << " ";
    return 0;
}