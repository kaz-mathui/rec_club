from typing import List, Dict


class Point:
    def __init__(self, r: int, c: int):
        """
        Point constructor.
        """
        self.row = r
        self.c = c


def gph(maze: List[List[bool]], row: int, col: int, path: List[Point],
        failed_points: Dict) -> bool:
    """
    Helper.
    """
    # If out of bounds or not available, return.
    if row < 0 or col < 0 or not maze[row][col]:
        return False
    p = Point(row, col)
    # If we've already visited this cell, return.
    if p in failed_points:
        return False
    is_at_origin = row == 0 and col == 0
    # If there's a path from start to my current location, add my location.
    if (is_at_origin
            or gph(maze, row, col - 1, path, failed_points)
            or gph(maze, row - 1, col, path, failed_points)):
        path.append(p)
        return True
    failed_points[p] = True
    return False


def get_path(maze: List[List[bool]]) -> List[Point]:
    """
    Gets path from top left corner of a maze to bottom right corner.
    """
    if maze is None or not len(maze):
        return None
    path = []
    failed_points = {}
    if gph(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


maze = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]

path = get_path(maze)
if path:
    for p in path:
        print(p.__dict__)
"""
{'row': 0, 'c': 0}
{'row': 0, 'c': 1}
{'row': 1, 'c': 1}
{'row': 2, 'c': 1}
{'row': 3, 'c': 1}
{'row': 3, 'c': 2}
{'row': 3, 'c': 3}
"""
