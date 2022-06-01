#include <iostream>
#include <vector>

using namespace std;

/**
 * Merges two sorted arrays.
 */
void merge(vector<int> &arr, int start, int mid, int end)
{
    vector<int> left(mid - start + 1);
    vector<int> right(end - mid);

    for (int i = 0; i < left.size(); i++)
        left[i] = arr[i + start];
    for (int i = 0; i < right.size(); i++)
        right[i] = arr[i + mid + 1];
    int l_index = 0, r_index = 0;
    int curr = start;
    while (l_index < left.size() && r_index < right.size())
    {
        if (left[l_index] <= right[r_index])
        {
            arr[curr] = left[l_index];
            l_index++;
        }
        else
        {
            arr[curr] = right[r_index];
            r_index++;
        }
        curr++;
    }
    while (l_index < left.size())
        arr[curr++] = left[l_index++];
    while (r_index < right.size())
        arr[curr++] = right[r_index++];
}

/**
 * Mergesort algorithm. 
 */
void merge_sort(vector<int> &arr, int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        merge_sort(arr, start, mid);
        merge_sort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

int main()
{
    vector<int> arr{9, 5, 8, 2, 4, 7, 1, 3, 6, 0};
    merge_sort(arr, 0, arr.size() - 1);
    for (auto i : arr)
        cout << i << " "; // 0 1 2 3 4 5 6 7 8 9
    return 0;
}