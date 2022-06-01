#include <stdio.h>

/**
 * Merge two sorted arrays using first array as a buffer.
 */
void merge(int a[], int b[], int last_a, int last_b)
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
    int i;
    int a[] = {0, 2, 4, 6, 8, 0, 0, 0, 0, 0, 0};
    int b[] = {-1, 1, 3, 6, 9, 12};
    int size = sizeof(a) / sizeof(int);

    merge(a, b, 5, 6);
    for (i = 0; i < size; i++)
        printf("%i ", a[i]);
    /* -1 0 1 2 3 4 6 6 8 9 12 */
    return 0;
}