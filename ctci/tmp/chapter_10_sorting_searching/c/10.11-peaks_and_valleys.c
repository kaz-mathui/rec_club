#include <stdio.h>
#include <limits.h>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

/**
 * Finds the max value of three given indexes in an array and returns the
 * associated index.
 */
int find_max(int *arr, int size, int prev, int curr, int next)
{
    int a = arr[prev], b = arr[curr];
    int c = next < size ? arr[next] : INT_MIN;
    int biggest = MAX(c, MAX(a, b));
    if (biggest == a)
        return prev;
    if (biggest == b)
        return curr;
    return next;
}

/**
 * Sorts an array into an alternating sequence of peaks and valleys.
 */
void sort_valley_peak(int *arr, int size)
{
    int i, tmp;

    for (i = 1; i < size; i += 2)
    {
        int m = find_max(arr, size, i - 1, i, i + 1);
        if (m != i)
        {
            tmp = arr[i];
            arr[i] = arr[m];
            arr[m] = tmp;
        }
    }
}

int main()
{

    int arr[] = {9, 1, 0, 4, 8, 7};
    int i, size = sizeof(arr) / sizeof(int);

    sort_valley_peak(arr, size);
    for (i = 0; i < size; i++)
        printf("%i ", arr[i]);
    printf("\n");
    /* 1 9 0 8 4 7 */

    int arr2[] = {-5, -4, 3};
    size = sizeof(arr2) / sizeof(int);
    sort_valley_peak(arr2, size);
    for (i = 0; i < size; i++)
        printf("%i ", arr2[i]);
    printf("\n");
    /* -5 3 4 */

    return 0;
}