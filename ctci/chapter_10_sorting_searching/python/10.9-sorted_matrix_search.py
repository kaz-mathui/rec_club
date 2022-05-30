from typing import List


class Coordinate():
    def __init__(self, r: int, c: int):
        """
        Coordinate constructor.
        """
        self.row = r
        self.col = c

    def is_inbounds(self, matrix: List[List[int]]) -> bool:
        """
        Determines if a Coordinate is within bounds of a given matrix.
        """
        return (self.row >= 0 and self.col >= 0 and self.row < len(matrix)
                and self.col < len(matrix[0]))

    def is_before(self, c) -> bool:
        """
        Determines if a Coordinate is before another Coordinate.
        """
        return self.row <= c.row and self.col <= c.col

    def clone(self):
        """
        Returns a clone of itself.
        """
        return Coordinate(self.row, self.col)

    def set_to_average(self, mininum, maximum):
        """
        Sets the row and column to be the average of two other Coordinates.
        """
        self.row = (mininum.row + maximum.row) // 2
        self.col = (mininum.col + maximum.col) // 2

    def __str__(self):
        """
        String representation.
        """
        return f"{self.__dict__}"


def find_element(matrix: List[List[int]], origin: Coordinate,
                 dest: Coordinate, x: int):
    """
    Helper.
    """
    if not origin.is_inbounds(matrix) or not dest.is_inbounds(matrix) or \
            not origin.is_before(dest):
        return None
    if matrix[origin.row][origin.col] == x:
        return origin

    # Set start to start of diagonal and end to the end of the diagonal. Since
    # the grid may not be square, the end of the diagonal may not equal dest.
    start = origin.clone()
    diag_dist = min(dest.row - origin.row, dest.col - origin.col)
    end = Coordinate(start.row + diag_dist, start.col + diag_dist)
    p = Coordinate(0, 0)

    # Do binary search on the diagonal, looking for the first element > x.
    while start.is_before(end):
        p.set_to_average(start, end)
        if x > matrix[p.row][p.col]:
            start.row = p.row + 1
            start.col = p.col + 1
        else:
            end.row = p.row - 1
            end.col = p.col - 1
    # Split the grid into quadrants. Search the bottom left and the top right.
    return partition_and_search(matrix, origin, dest, start, x)


def partition_and_search(matrix: List[List[int]],
                         origin: Coordinate, dest: Coordinate,
                         pivot: Coordinate, x: int) -> Coordinate:
    """
    Partitions matrix into quadrants and search lower-left and upper-right
    quadrants.
    """
    lower_left_origin = Coordinate(pivot.row, origin.col)
    lower_left_dest = Coordinate(dest.row, pivot.col - 1)
    upper_right_origin = Coordinate(origin.row, pivot.col)
    upper_right_dest = Coordinate(pivot.row - 1, dest.col)

    lower_left = find_element(matrix, lower_left_origin, lower_left_dest, x)
    if lower_left == None:
        return find_element(matrix, upper_right_origin, upper_right_dest, x)
    return lower_left


def find(matrix: List[List[int]], x: int) -> Coordinate:
    """
    Given an m x n matrix, finds the row and column of an element.
    """
    origin = Coordinate(0, 0)
    dest = Coordinate(len(matrix) - 1, len(matrix[0]) - 1)
    return find_element(matrix, origin, dest, x)


matrix = [
    [15, 20, 70, 85],
    [25, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 120, 120]
]

print(find(matrix, 15))  # {'row': 0, 'col': 0}
print(find(matrix, 85))  # {'row': 0, 'col': 3}
print(find(matrix, 120))  # {'row': 3, 'col': 2}
