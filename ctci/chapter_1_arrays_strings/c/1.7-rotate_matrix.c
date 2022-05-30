#include <stdio.h>

/* O(n**2) solution, best case scenario  */

/* Need to set macro for matrix size. */
#define MATRIX_SIZE 4

/**
 * Prints matrix row by row.
 */
void print_matrix(int *matrix, int length)
{
    int i, j;

    for (i = 0; i < length; i++)
        for (j = 0; j < length; j++)
        {
            printf("%02i", *(matrix + (i * length) + j));
            j == length - 1
                ? printf("\n")
                : printf(", ");
        }
    printf("===============\n");
}

/**
 * Rotates a NxN matrix 90 degrees in place.
 */
void rotate_matrix(int (*matrix)[MATRIX_SIZE])
{
    int layer, first, last, n, i, offset, top;

    n = MATRIX_SIZE;
    for (layer = 0; layer < n / 2; layer++)
    {
        first = layer;
        last = n - 1 - layer;
        offset = 0;
        for (i = first; i < last; i++)
        {
            // /* remove top */
            top = matrix[first][i];
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