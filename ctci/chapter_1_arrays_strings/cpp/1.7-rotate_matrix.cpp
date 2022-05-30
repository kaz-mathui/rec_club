#include <iostream>
#include <stdio.h>

/* O(n**2) solution, best case scenario  */

using namespace std;

/* Need to set macro for matrix size. */
#define MATRIX_SIZE 4

/**
 * Prints matrix row by row.
 */
void print_matrix(int *matrix, int length)
{
    for (int i = 0; i < length; i++)
        for (int j = 0; j < length; j++)
        {
            printf("%02i", *(matrix + (i * length) + j));
            j == length - 1
                ? cout << endl
                : cout << ", ";
        }
    cout << "===============\n";
}

/**
 * Rotates a NxN matrix 90 degrees in place.
 */
void rotate_matrix(int (*matrix)[MATRIX_SIZE])
{
    int n = MATRIX_SIZE;

    for (int layer = 0; layer < n / 2; layer++)
    {
        int first = layer;
        int last = n - 1 - layer;
        int offset = 0;
        for (int i = first; i < last; i++)
        {
            // /* remove top */
            int top = matrix[first][i];
            // /* left -> top */
            matrix[first][i] = matrix[last - offset][first];
            // /* bottom -> left */
            matrix[last - offset][first] = matrix[last][last - offset];
            // /* right -> bottom */
            matrix[last][last - offset] = matrix[i][last];
            // /* top -> right */
            matrix[i][last] = top;
            offset++;
        }
    }
}

int main()
{
    int matrix3[4][4] = {
        {0, 1, 2, 3},
        {4, 5, 6, 7},
        {8, 9, 10, 11},
        {12, 13, 14, 15},
    };

    print_matrix((int *)matrix3, 4);
    rotate_matrix(matrix3);
    print_matrix((int *)matrix3, 4);

    return 0;
}