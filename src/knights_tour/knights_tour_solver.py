from typing import List, Tuple, Optional

from src.knights_tour.board import Board, Position, Move, BoardSize
from src.knights_tour.board_visualizer import BoardVisualizer


class KnightsTourSolver:
    """
    A class to solve the Knight's Tour problem using backtracking with Warnsdorff's rule.
    """

    # Possible moves for a knight
    MOVES: List[Move] = [
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
        size: Tuple,
        start: Tuple,
        visualize: bool = False,
        loop: bool = False,
    ):
        """
        Initializes the KnightsTourSolver with the given board size, starting position, and options.

        Args:
            size (Tuple[int, int]): Size of the chessboard (rows, cols).
            start (Tuple[int, int]): Starting position of the knight (x, y).
            visualize (bool): Whether to visualize the knight's tour live.
            loop (bool): Whether to allow looping of the knight's tour.
        """
        self.size = BoardSize(*size)
        self.start = Position(*start)
        self.visualizer = BoardVisualizer(visualize)
        self.loop = loop

        # Create board state with knight at starting position
        board = Board(self.size)
        board.set(self.start)

        # Initialize stack with starting board state
        self.stack = [board]

    def solve(self) -> None:
        """
        Solves the Knight's Tour problem and prints the solution if found.
        """
        solved_board = self._solve_knight_tour()
        if solved_board:
            self.visualizer.print_board(solved_board)
        else:
            print("No solution found")

        self.visualizer.close()

    def _solve_knight_tour(self) -> Optional[Board]:
        """
        Solves the Knight's Tour problem using backtracking.

        Returns:
            Optional[Board]: The solution board if found, None otherwise.
        """
        while self.stack:
            board = self.stack.pop()

            # Update the plot if visualization is enabled
            self.visualizer.plot_board(board)

            # Solution found if board max moves reached
            if board.move_count == self._get_max_moves(board):
                return board

            # Sort possible moves based on Warnsdorff's rule
            next_moves = sorted(
                self.MOVES,
                key=lambda move: self._get_degree(
                    self._get_next_position(board.current_position(), move), board
                ),
            )

            # Reverse the moves to prioritize moves with lower degree at the top of the stack
            next_moves.reverse()

            # Add all valid next moves to the stack
            for move in next_moves:
                next_position = self._get_next_position(board.current_position(), move)

                if self._is_valid_move(next_position, board):
                    # Create new board state for stack
                    new_board = board.copy()
                    new_board.set(next_position)
                    self.stack.append((new_board))

        # No solution found
        return None

    def _is_valid_move(self, position: Position, board: Board) -> bool:
        """
        Checks if the move to the position (x, y) is valid.

        Args:
            position: Position[int, int]: (x, y) coordinate of the next position.
            board Board: The current state of the board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (board.is_valid_position(position) and board.get(position) == -1) or (
            self.loop
            and position == self.start
            and board.move_count == self._get_max_moves(board) - 1
        )

    def _get_degree(self, position: Position, board: Board) -> int:
        """
        Returns the degree of the given new Position based on Warnsdorff's rule.

        Args:
            position (Position[int, int]): Position to calculate the degree for.
            board (Board): The current board state.
        """
        count = 0
        for move in self.MOVES:
            next_position = self._get_next_position(position, move)
            if self._is_valid_move(next_position, board):
                count += 1
        return count

    def _get_next_position(self, position: Position, move: Move) -> Position:
        """
        Returns the next position after applying the given move.

        Args:
            position (Position): Current position.
            move (Move): Move to apply to the position.

        Returns:
            Position: The next position after applying the move.
        """
        return Position(position.x + move.dx, position.y + move.dy)

    def _get_max_moves(self, board: Board) -> int:
        """
        Returns the maximum number of moves for the knight's tour.

        Args:
            board (Board): The current board state.
        """
        return (
            board.size.rows * board.size.cols
            if not self.loop
            else board.size.rows * board.size.cols + 1
        )
