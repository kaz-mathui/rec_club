#include <iostream>
#include <vector>

using namespace std;

/**
 * Moves all elements smaller than pivot to the left of it and places pivot in
 * correct location in array. Returns new index of pivot.
 */
int partition(vector<int> &arr, int low, int high)
{
    int i = low - 1;
    int pivot = arr[high];
    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

/**
 * Quicksort algorithm. 
 */
void quicksort(vector<int> &arr, int start, int end)
{
    if (start < end)
    {
        int p = partition(arr, start, end);
        quicksort(arr, p + 1, end);
        quicksort(arr, start, p - 1);
    }
}

int main()
{
    vector<int> arr{9, 5, 8, 2, 4, 7, 1, 3, 6, 0};
    quicksort(arr, 0, arr.size() - 1);
    for (auto i : arr)
        cout << i << " "; // 0 1 2 3 4 5 6 7 8 9
    return 0;
}