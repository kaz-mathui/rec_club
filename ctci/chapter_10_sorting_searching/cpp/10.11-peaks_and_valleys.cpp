#include <iostream>
#include <vector>
#include <climits>

using namespace std;

/**
 * Finds the max value of three given indexes in an array and returns the
 * associated index.
 */
int find_max(vector<int> &arr, int prev, int curr, int next)
{
    int a = arr[prev], b = arr[curr];
    int c = next < arr.size() ? arr[next] : INT_MIN;
    int biggest = max(c, max(a, b));
    if (biggest == a)
        return prev;
    if (biggest == b)
        return curr;
    return next;
}

/**
 * Sorts an array into an alternating sequence of peaks and valleys.
 */
void sort_valley_peak(vector<int> &arr)
{
    for (int i = 1; i < arr.size(); i += 2)
    {
        int m = find_max(arr, i - 1, i, i + 1);
        if (m != i)
            swap(arr[i], arr[m]);
    }
}

int main()
{

    vector<int> arr{9, 1, 0, 4, 8, 7};
    sort_valley_peak(arr);
    for (auto i : arr)
        cout << i << " ";
    cout << endl;
    /* 1 9 0 8 4 7 */

    vector<int> arr2{-5, -4, 3};
    sort_valley_peak(arr2);
    for (auto i : arr2)
        cout << i << " ";
    cout << endl;
    /* -5 3 4 */

    return 0;
}