from enum import Enum, auto
from typing import List


class Color(Enum):
    BLACK = auto()
    WHITE = auto()
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

    def __str__(self):
        return f"{self.name}"


def paint_fill(screen: List[List[Color]], r: int, c: int,
               ncolor: Color) -> bool:
    """
    Given a screen (represented by a two-dimensional array of colors), a point
    and a new color, fill in the surrounding area until the color changes from
    the original color.
    """
    if screen[r][c] == ncolor:
        return False
    return paint_fill_helper(screen, r, c, screen[r][c], ncolor)


def paint_fill_helper(screen: List[List[Color]], r: int, c: int, ocolor: Color,
                      ncolor: Color) -> bool:
    """
    Helper.
    """
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
        return False
    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        paint_fill_helper(screen, r - 1, c, ocolor, ncolor)  # up
        paint_fill_helper(screen, r + 1, c, ocolor, ncolor)  # down
        paint_fill_helper(screen, r, c - 1, ocolor, ncolor)  # left
        paint_fill_helper(screen, r, c + 1, ocolor, ncolor)  # right
    return True


screen = [[Color.BLACK] * 4] * 4
print([[str(y) for y in x] for x in screen])
"""
[
    ['BLACK', 'BLACK', 'BLACK', 'BLACK'],
    ['BLACK', 'BLACK', 'BLACK', 'BLACK'],
    ['BLACK', 'BLACK', 'BLACK', 'BLACK'],
    ['BLACK', 'BLACK', 'BLACK', 'BLACK']
]
"""
paint_fill(screen, 0, 0, Color.WHITE)
print([[str(y) for y in x] for x in screen])
"""
[
    ['WHITE', 'WHITE', 'WHITE', 'WHITE'],
    ['WHITE', 'WHITE', 'WHITE', 'WHITE'],
    ['WHITE', 'WHITE', 'WHITE', 'WHITE'],
    ['WHITE', 'WHITE', 'WHITE', 'WHITE']
]
"""
