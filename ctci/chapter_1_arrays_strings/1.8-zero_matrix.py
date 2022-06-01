from typing import List

# O(n**2) solution, best case


def set_zeros(matrix: List[List[int]]):
    """
    Sets zeros for all values in same row and column as existing zeroes.
    """
    rows = []
    columns = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)
    for r in rows:
        nullify_row(matrix, r)
    for c in columns:
        nullify_column(matrix, c)


def nullify_row(matrix: List[List[int]], row: int):
    """
    Set zeros for all values in a given row of a matrix.
    """
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_column(matrix: List[List[int]], column: int):
    """
    Set zeros for all values in a given column of a matrix.
    """
    for i in range(len(matrix)):
        matrix[i][column] = 0


def print_matrix(matrix: List[List[int]]):
    """
    Prints matrix row by row.
    """
    for m in matrix:
        print(m)
    print('====================')


if __name__ == "main":
    matrix1 = [
        [2, 2, 2, 2, 2],
        [2, 2, 0, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2]
    ]

    print_matrix(matrix1)
    set_zeros(matrix1)
    print_matrix(matrix1)
