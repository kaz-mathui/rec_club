from typing import List


def rotate_matrix_by_90(matrix: List[List[int]]) -> bool:
    """ 
    Rotates a NxN matrix 90 degrees in place.
    """
    if not len(matrix) or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        offset = 0
        for i in range(first, last):
            # extract top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
            offset += 1
    return True


def print_matrix(matrix: List[List[int]]):
    """
    Prints matrix row by row.
    """
    for m in matrix:
        print(m)
    print('====================')


if __name__ == "__main__":
    matrix1 = [[0, 1], [2, 3]]
    matrix2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    matrix3 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    matrix4 = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24]
    ]

    print_matrix(matrix1)
    rotate_matrix_by_90(matrix1)
    print_matrix(matrix1)

    print_matrix(matrix2)
    rotate_matrix_by_90(matrix2)
    print_matrix(matrix2)

    print_matrix(matrix3)
    rotate_matrix_by_90(matrix3)
    print_matrix(matrix3)

    print_matrix(matrix4)
    rotate_matrix_by_90(matrix4)
    print_matrix(matrix4)
