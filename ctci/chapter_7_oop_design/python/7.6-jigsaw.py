from enum import Enum, auto
from typing import List


class Orientation(Enum):
    LEFT = auto()
    TOP = auto()
    RIGHT = auto()
    BOTTOM = auto()

    def get_opposite(self):
        """
        Get opposite side.
        """
        if self == self.LEFT:
            return self.RIGHT
        if self == self.RIGHT:
            return self.LEFT
        if self == self.TOP:
            return self.BOTTOM
        if self == self.BOTTOM:
            return self.TOP


class Shape(Enum):
    INNER = auto()
    OUTER = auto()
    FLAT = auto()

    def get_opposite(self):
        """
        Get opposite side.
        """
        if self == self.INNER:
            return self.OUTER
        if self == self.OUTER:
            return self.INNER


class Puzzle:
    def __init__(self, size: int, pieces):
        """
        Puzzle constructor.
        """
        self.solution = []
        self.size = size
        self.pieces = {}

    def set_edge_in_solution(self, pieces: List, e, row: int, column: int,
                             o: Orientation):
        """
        Put piece into the solution, turn it appropriately, and remove from
        list.
        """
        piece = e.parent_piece
        piece.set_edge_as_orientation(e, o)
        del self.pieces[piece]
        self.solution[row][column] = piece


class Piece:
    def __init__(self, edge_list: List):
        """
        Piece constructor.
        """
        self.edges = {}

    def rotate_edges_by(self, number_rotations: int):
        """
        Rotates edges by a number of times.
        """
        pass

    def set_edge_as_orientation(self, e, o: Orientation):
        """
        Sets an edge as an orientation.
        """
        pass

    def is_corner(self):
        """
        Determines if piece is a corner piece.
        """
        pass

    def is_border(self):
        """
        Determines if piece is a border piece.
        """
        pass


class Edge:
    def __init__(self):
        """
        Edge constructor.
        """
        self.shape = None
        self.parent_piece = None

    def fits_with(self):
        """
        Determines if edge fits with another edge.
        """
        pass

# Solution


def fit_next_edge(pieces_to_search: List, row: int, column: int):
    """
    Fits the next edge.
    """
    # On top left corner, just put in a piece.
    if row == 0 and column == 0:
        p = pieces_to_search.remove()
        orient_top_left_corner()
        solution[0][0] = p
    else:
        # Get the right edge and list to match.
        if column == 0:
            piece_to_match = solution[row - 1][0]
            orientation_to_match = Orientation.BOTTOM
        else:
            piece_to_match = solution[row][column - 1]
            orientation_to_match = Orientation.RIGHT

        # Get matching edge.
        edge = get_matching_edge(edge_to_match, pieces_to_search)
        if not edge:  # Can't solve.
            return False
        # Insert piece and edge.
        orientation = orientation_to_match.get_opposite()
        set_edge_in_solution(pieces_to_search, edge, row, column, orientation)
    return True


def solve():
    """
    Solves the puzzle.
    """
    # Group pieces
    corner_pieces = []
    border_pieces = []
    inside_pieces = []
    group_pieces(corner_pieces, border_pieces, inside_pieces)

    # Walk through puzzle, finding the piece that joins the previous one.
    solution = []
    for i in range(len(size)):
        for j in range(len(column)):
            pieces_to_search = get_piece_list_to_search(
                corner_pieces, border_pieces, inside_pieces, row, column)
            if not fit_next_edge(pieces_to_search, row, column):
                return False
    return True
