#include <iostream>
#include <stdio.h>

/* O(n**2) solution, best case */

using namespace std;

#define COLUMN_SIZE 3
#define ROW_SIZE 4

/** 
 * Prints matrix row by row. 
 */
void print_matrix(int matrix[COLUMN_SIZE][ROW_SIZE])
{
    for (int i = 0; i < COLUMN_SIZE; i++)
        for (int j = 0; j < ROW_SIZE; j++)
        {
            printf("%i", matrix[i][j]);
            j == COLUMN_SIZE
                ? cout << endl
                : cout << ", ";
        }
    cout << "===============\n";
}

/**
 * Set zeros for all values in a given row of a matrix.
 */
void nullify_row(int matrix[COLUMN_SIZE][ROW_SIZE], int row)
{
    for (int i = 0; i < ROW_SIZE; i++)
        matrix[row][i] = 0;
}

/**
 * Set zeros for all values in a given column of a matrix.
 */
void nullify_column(int matrix[COLUMN_SIZE][ROW_SIZE], int column)
{
    for (int i = 0; i < COLUMN_SIZE; i++)
        matrix[i][column] = 0;
}

/**
 * Sets zeros for all values in same row and column as existing zeroes.
 */
void set_zeros(int matrix[COLUMN_SIZE][ROW_SIZE])
{
    int columns[COLUMN_SIZE] = {0};
    int rows[ROW_SIZE] = {0};

    for (int i = 0; i < COLUMN_SIZE; i++)
        for (int j = 0; j < ROW_SIZE; j++)
            if (matrix[i][j] == 0)
            {
                columns[i] = 1;
                rows[j] = 1;
            }
    for (int i = 0; i < ROW_SIZE; i++)
        if (rows[i] == 1)
            nullify_column(matrix, i);
    for (int i = 0; i < COLUMN_SIZE; i++)
        if (columns[i] == 1)
            nullify_row(matrix, i);
}

int main(void)
{
    int matrix[3][4] = {
        {2, 2, 2, 2},
        {2, 2, 2, 2},
        {2, 2, 0, 2}};

    print_matrix(matrix);
    set_zeros(matrix);
    print_matrix(matrix);

    return 0;
}