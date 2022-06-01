from enum import Enum, auto
from random import randint


class GameState(Enum):
    WON: auto()
    LOST: auto()
    RUNNING: auto()


class Cell:
    def __init__(self, r: int, c: int):
        """
        Cell constructor.
        """
        self.row = r
        self.column = c
        self.is_bomb = False
        self.number = 0
        self.is_exposed = False
        self.is_guess = False
        self.is_blank = False

    def flip(self) -> bool:
        """
        Toggles cell.
        """
        self.is_exposed = True
        return not self.is_bomb

    def toggle_guess(self) -> bool:
        """
        Toggles guess attribute.
        """
        if not self.is_exposed:
            self.is_guess = not self.is_guess
        return self.is_guess


class UserPlay:
    def __init__(self):
        """
        UserPlay constructor.
        """
        self.row = 0
        self.column = 0
        self.is_guess = False


class UserPlayResult:
    def __init__(self):
        """
        UserPlayResult constructor.
        """
        self.succesful = False
        self.resulting_state = None


class Board:
    def __init__(self, c: int, r: int, b: int):
        """
        Board constructor.
        """
        self.n_rows = r
        self.n_columns = c
        self.n_bombs = b
        self.cells = []
        self.bombs = []
        self.num_unexposed_remaining = 0

    def initialize_board(self): pass
    def flip_cell(self, c: Cell): pass
    def play_flip(self, play: UserPlay): pass
    def in_bounds(self, r: int, c: int): pass

    def shuffle_board(self):
        """
        Shuffle the board.
        """
        n_cells = self.n_rows * self.n_columns
        for i in range(n_cells):
            j = i + randint(0, n_cells - i)
            if i != j:
                # Get cell at i
                row1 = i // self.n_columns
                column1 = (i - row1 * self.n_columns) % self.n_columns
                cell1 = self.cells[row1][column1]

                # Get cell at j
                row2 = j / self.n_columns
                column2 = (j - row2 * self.n_columns) % self.n_columns
                cell2 = self.cells[row2][column2]

                # Swap
                self.cells[row1][column2] = cell2
                cell2.set_row_and_column(row1, column1)
                self.cells[row2][column2] = cell1
                cell1.set_row_and_column(row2, column2)

    def set_numbered_cells(self):
        """
        Set the cells around the bombs to the right number. Although the bombs have been shuffled, the reference in the bombs array is still to same object.
        """
        deltas = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        for b in self.bombs:
            row = b["row"]
            col = b["col"]
            for d in deltas:
                r = row + d[0]
                c = col + d[1]
                if self.in_bounds(r, c):
                    self.cells[r][c].increment_number()

    def expand_blank(self, cell: Cell):
        """
        Expand a blank region.
        """
        deltas = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        to_explore_queue = [cell]
        while len(to_explore_queue):
            curr = to_explore_queue.pop(0)
            for d in deltas:
                r = curr["row"] + d[0]
                c = curr["col"] + d[1]
                if self.in_bounds(r, c):
                    neighbor = self.cells[r][c]
                    if self.flip_cell(neighbor) and neighbor.is_blank():
                        to_explore_queue.append(neighbor)


class Game:
    def __init__(self, r: int, c: int, b: int):
        """
        Game constructor.
        """
        self.board = None
        self.rows = r
        self.columns = c
        self.bombs = b
        self.state = None

    def initialize(self): pass
    def start(self): pass
    def play_game(self): pass
