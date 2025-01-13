from typing import List, Tuple

from src.knights_tour.board import Board, Position, Move, BoardSize


class KnightsTourSolver:
    """
    A class to solve the Knight's Tour problem using backtracking with Warnsdorff's rule.
    """

    # Possible moves for a knight
    MOVES: List[Move[int, int]] = [
        Move(dx, dy)
        for dx, dy in [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ]
    ]

    def __init__(
        self,
        size: Tuple[int, int],
        start: Tuple[int, int],
        visualize: bool = False,
        loop: bool = False,
    ):
        """
        Initializes the KnightsTourSolver with the given board size, starting position, and options.

        Args:
            size (Tuple[int, int]): Size of the chessboard (rows, cols).
            start (Tuple[int, int]): Starting position of the knight (x, y).
            visualize (bool): Whether to visualize the knight's tour.
            loop (bool): Whether to allow looping of the knight's tour.
        """
        self.start = Position(*start)
        self.size = BoardSize(*size)

        self.board = Board(self.size, visualize=visualize)

        # Place the knight at the starting position
        self.board.set(self.start, 0)
        self.path = [self.start]

        self.visualize = visualize

        self.loop = loop

    def solve(self) -> None:
        """
        Solves the Knight's Tour problem and prints the solution if found.
        """
        if self._solve_knight_tour(self.start, 1):
            self.board.print_board()
        else:
            print("No solution found")

        self.board.close()

    def _is_valid_move(self, position: Position[int, int], move_count: int) -> bool:
        """
        Checks if the move to the position (x, y) is valid.

        Args:
            position: Position[int, int]: (x, y) coordinate of the next position.
            move_count (int): The current move count.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (
            0 <= position.x < self.size.rows
            and 0 <= position.y < self.size.cols
            and self.board.get(position) == -1
        ) or (
            self.loop
            and position == self.start
            and move_count == self._get_max_moves() - 1
        )

    def _get_degree(self, position: Position[int, int], move_count: int) -> int:
        """
        Returns the degree of the given position based on Warnsdorff's rule.

        Args:
            position (Position[int, int]): Position to calculate the degree for.
            move_count (int): The current move count.
        """
        count = 0
        for move in self.MOVES:
            next_position = self._get_next_position(position, move)
            if self._is_valid_move(next_position, move_count):
                count += 1
        return count

    def _get_max_moves(self) -> int:
        """
        Returns the maximum number of moves for the knight's tour.
        """
        return (
            self.size.rows * self.size.cols
            if not self.loop
            else self.size.rows * self.size.cols + 1
        )

    def _get_next_position(self, position: Position[int, int], move: Move[int, int]):
        """
        Returns the next position after applying the given move.
        """
        return Position(position.x + move.dx, position.y + move.dy)

    def _solve_knight_tour(self, position: Position[int, int], move_count: int) -> bool:
        """
        Recursively solves the Knight's Tour problem using backtracking.

        Args:
            position (Position[int, int]): Current position of the knight.
            move_count (int): Current move count.
        """
        if move_count == self._get_max_moves():
            return True

        # Sort moves based on Warnsdorff's rule
        next_moves = sorted(
            self.MOVES,
            key=lambda move: self._get_degree(
                self._get_next_position(position, move), move_count
            ),
        )

        for move in next_moves:
            next_position = self._get_next_position(position, move)

            if self._is_valid_move(next_position, move_count):
                self.board.set(next_position, move_count)

                # Update the plot if visualization is enabled
                if self.visualize:
                    self.board.plot_board()

                if self._solve_knight_tour(next_position, move_count + 1):
                    return True

                # Backtrack
                self.board.unset(next_position)

        return False
