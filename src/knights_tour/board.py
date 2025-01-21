import numpy as np
from typing import List, NamedTuple


# Represent the size of the chessboard
class BoardSize(NamedTuple):
    rows: int
    cols: int


# Represent a position on the chessboard
class Position(NamedTuple):
    x: int
    y: int


# Represent a move on the chessboard
class Move(NamedTuple):
    dx: int
    dy: int


# Represents the chessboard state and history of the knight
class Board:
    def __init__(
        self,
        size: BoardSize,
    ):
        """
        Initializes the Board with the given board size.

        Args:
            size (Tuple[int, int]): Size of the chessboard (rows, cols).
            visualize (bool): Whether to visualize the board state.
        """
        self.size = size

        # Initialize the chessboard
        self.board = np.full((self.size.rows, self.size.cols), -1, dtype=int)
        self.path: List[Position] = []
        self.move_count = 0

    def set(self, pos: Position) -> None:
        """
        Sets the the current position of the knight

        Args:
            pos (Position[int, int]): Position of the cell (x, y).
        """
        self.board[pos.x][pos.y] = self.move_count
        self.path.append(pos)
        self.move_count += 1

    def get(self, pos: Position) -> int:
        """
        Gets the move count of the cell at the given position.

        Args:
            pos (Position[int, int]): Position of the cell (x, y).

        Returns:
            int: Move count value of the cell.
        """
        return self.board[pos.x][pos.y]

    def current_position(self) -> Position:
        """
        Returns the current position of the knight.
        """
        return self.path[-1]

    def rows(self) -> List:
        return self.board.tolist()

    def is_valid_position(self, position: Position) -> bool:
        """
        Checks if the position is valid on the board.
        """
        return 0 <= position.x < self.size.rows and 0 <= position.y < self.size.cols

    def copy(self) -> "Board":
        """
        Returns a copy of the board state.
        """
        board_copy = Board(self.size)
        board_copy.board = self.board.copy()
        board_copy.path = self.path.copy()
        board_copy.move_count = self.move_count

        return board_copy
