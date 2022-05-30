from typing import List


def place_queens(row: int, columns: List[int], results: List[List[int]]):
    """
    Finds all ways of arranging queens on a 8x8 chess board so that none of
    them share the same row, column or diagonal.
    """
    GRID_SIZE = 8
    if row == GRID_SIZE:  # Found valid placement.
        results.append(columns[:])
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col  # Place queen.
                place_queens(row + 1, columns, results)


def check_valid(columns: List[int], row1: int, column1: int) -> bool:
    """
    Check if (row1, column1) is a valid spot for a queen by checking if
    there is a queen in the same column or diagonal. We don't need to
    check for queens in the same row because the calling place_queens
    only attempts to place one queen at a time. We know this row is empty.
    """
    for row2 in range(row1):
        column2 = columns[row2]
        # Check if (row2, column2) invalidates (row1, column1) as a queen spot.
        # Check if rows have a queen in the same column.
        if column1 == column2:
            return False
        # Check diagonals: if the distance between the columns equals the
        # distance between the rows, then they're in the same diagonals.
        column_distance = abs(column2 - column1)
        # row1 > row2, so no need for abs.
        row_distance = row1 - row2
        if column_distance == row_distance:
            return False
    return True
