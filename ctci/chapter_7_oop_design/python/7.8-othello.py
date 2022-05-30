from enum import Enum, auto


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Color(Enum):
    WHITE = auto()
    BLACK = auto()


class Piece:
    def __init__(self, c: Color = None):
        """
        Piece constructor.
        """
        self.color = c

    def flip(self):
        """
        Flip color.
        """
        if self.color == Color.BLACK:
            self.color = Color.WHITE
        else:
            self.color = Color.BLACK


class Board:
    def __init__(self, rows: int, columns: int):
        """
        Board constructor.
        """
        self.black_count = 0
        self.white_count = 0
        self.board = [0 * rows] * columns

    def initialize(self):
        """
        Initialize center black and white pieces.
        """
        pass

    def place_color(self, row: int, column: int, color: Color):
        """
        Attempt to place a piece of color at (row, column). Return true if we we were successful.
        """
        pass

    def flip_section(self, row: int, column: int, color: Color, d: Direction):
        """
        Flip pieces starting at (row, column) and proceeding in direction d.
        """
        pass

    def get_score_for_color(self, c: Color) -> int:
        """
        Get score for color.
        """
        if c == Color.BLACK:
            return self.black_count
        return self.white_count

    def update_score(self, new_color: Color, new_pieces: int):
        """
        Update board with additional new_pieces pieces of color new_color. Decrease score of opposite color.
        """
        pass


class Player:
    def __init__(self, c: Color):
        """
        Player constructor.
        """
        self.color = c

    def get_score(self): pass

    def play_piece(self, r: int, c: int) -> bool:
        """
        Play a piece on the board.
        """
        return Game().board.place_color(r, c, self.color)


class Game:
    instance = None  # static

    def __init__(self):
        """
        Game constructor.
        """
        self.players = [None, None]
        self.rows = 10
        self.columns = 10
        self.board = Board(self.rows, self.columns)
        self.players[0] = Player(Color.BLACK)
        self.players[1] = Player(Color.WHITE)

    def __new__(cls, *args, **kwargs):
        """
        Gets game instance. Singleton design pattern.
        """
        if cls.instance == None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


g1 = Game()
g2 = Game()
print(g1 == g2)  # True
