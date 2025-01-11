import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


class KnightsTourSolver:
    """
    A class to solve the Knight's Tour problem using backtracking with Warnsdorff's rule.
    """

    # Possible moves for a knight
    MOVES: List[Tuple[int, int]] = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
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
        self.rows, self.cols = size
        self.start_x, self.start_y = start

        # Initialize the chessboard
        self.board = np.full((self.rows, self.cols), -1, dtype=int)

        # Place the knight at the starting position
        self.board[self.start_x][self.start_y] = 0
        self.path_x = [self.start_y + 0.5]
        self.path_y = [self.start_x + 0.5]

        self.visualize = visualize
        self.loop = loop

        self.fig, self.ax = plt.subplots() if self.visualize else (None, None)

    def solve(self) -> None:
        """
        Solves the Knight's Tour problem and prints the solution if found.
        """
        plt.ion()  # Turn on interactive mode if visualization is enabled

        if self._solve_knight_tour(self.start_x, self.start_y, 1):
            self._print_board()
        else:
            print("No solution found")

        # Turn off interactive mode
        if self.visualize:
            plt.ioff()
            plt.show()

    def _is_valid_move(self, x: int, y: int, move_count: int) -> bool:
        """
        Checks if the move to the position (x, y) is valid.

        Args:
            x (int): X-coordinate of the move.
            y (int): Y-coordinate of the move.
            move_count (int): The current move count.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (
            0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y] == -1
        ) or (
            self.loop
            and x == self.start_x
            and y == self.start_y
            and move_count == self._get_max_moves() - 1
        )

    def _get_degree(self, x: int, y: int, move_count: int) -> int:
        count = 0
        for move in self.MOVES:
            next_x, next_y = x + move[0], y + move[1]
            if self._is_valid_move(next_x, next_y, move_count):
                count += 1
        return count

    def _get_max_moves(self) -> int:
        return self.rows * self.cols if not self.loop else self.rows * self.cols + 1

    def _solve_knight_tour(self, x: int, y: int, move_count: int) -> bool:
        if move_count == self._get_max_moves():
            return True

        # Sort moves based on Warnsdorff's rule
        next_moves = sorted(
            self.MOVES,
            key=lambda move: self._get_degree(x + move[0], y + move[1], move_count),
        )

        for move in next_moves:
            next_x, next_y = x + move[0], y + move[1]

            if self._is_valid_move(next_x, next_y, move_count):
                self.board[next_x][next_y] = move_count
                self.path_x.append(next_y + 0.5)
                self.path_y.append(next_x + 0.5)

                # Update the plot if visualization is enabled
                if self.visualize:
                    self._plot_board()

                if self._solve_knight_tour(next_x, next_y, move_count + 1):
                    return True

                # Backtrack
                self.board[next_x][next_y] = -1
                self.path_x.pop()
                self.path_y.pop()

                # Update the plot if visualization is enabled
                if self.visualize:
                    self._plot_board()

        return False

    def _print_board(self) -> None:
        for row in self.board:
            print(" ".join(str(cell).rjust(2, "0") for cell in row))
        print()

    def _plot_board(self) -> None:
        self.ax.clear()
        self.ax.set_xticks(np.arange(self.cols))
        self.ax.set_yticks(np.arange(self.rows))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(True)

        # Create a checkerboard pattern
        for i in range(self.rows):
            for j in range(self.cols):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.ax.add_patch(
                    plt.Rectangle(
                        (j, i), 1, 1, linewidth=2, edgecolor="black", facecolor=color
                    )
                )
                # Add the move number to the cell
                if self.board[i][j] != -1:
                    self.ax.text(
                        j + 0.5,
                        i + 0.5,
                        str(self.board[i][j]).rjust(2, "0"),
                        ha="center",
                        va="center",
                        color="black",
                    )

        # Create a gradient color for the path
        for i in range(len(self.path_x) - 1):
            self.ax.plot(
                self.path_x[i : i + 2],
                self.path_y[i : i + 2],
                color=plt.cm.coolwarm(i / (self.rows * self.cols - 1)),
                marker="o",
            )

        plt.gca().invert_yaxis()
        plt.draw()
        plt.pause(0.01)
