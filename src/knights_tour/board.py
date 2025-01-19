import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes
from typing import List, Optional, NamedTuple


class BoardSize(NamedTuple):
    rows: int
    cols: int


class Position(NamedTuple):
    x: int
    y: int


class Move(NamedTuple):
    dx: int
    dy: int


class Board:
    def __init__(
        self,
        size: BoardSize,
        visualize: bool = False,
    ):
        """
        Initializes the Board with the given board size.

        Args:
            size (Tuple[int, int]): Size of the chessboard (rows, cols).
            visualize (bool): Whether to visualize the board state.
        """
        self.size = size
        self.visualize = visualize

        # Initialize the chessboard
        self.board = np.full((self.size.rows, self.size.cols), -1, dtype=int)
        self.path: List[Position] = []
        self.fig: Optional[Figure] = None
        self.ax: Optional[Axes] = None

        if self.visualize:
            self.fig, self.ax = plt.subplots()
            plt.ion()

    def set(self, pos: Position, value: int) -> None:
        """
        Sets the value of the cell at the given position.

        Args:
            pos (Position[int, int]): Position of the cell (x, y).
            value (int): Value to set.
        """
        self.board[pos.x][pos.y] = value
        self.path.append(pos)

    def unset(self, pos: Position) -> None:
        """
        Unsets the value of the cell at the given position.

        Args:
            pos (Position[int, int]): Position of the cell (x, y).
        """
        self.board[pos.x][pos.y] = -1
        self.path.pop()

    def get(self, pos: Position) -> int:
        """
        Gets the value of the cell at the given position.

        Args:
            pos (Position[int, int]): Position of the cell (x, y).

        Returns:
            int: Value of the cell.
        """
        return self.board[pos.x][pos.y]

    def rows(self) -> List:
        return self.board.tolist()

    def print_board(self) -> None:
        """
        Prints the board state.
        """
        max_num = self.size.rows * self.size.cols - 1
        width = len(str(max_num))
        for row in self.board:
            print(" ".join(str(cell).rjust(width, "0") for cell in row))
        print()

    def plot_board(self) -> None:
        """
        Plots the board state using matplotlib.
        """
        if self.ax is None:
            raise RuntimeError("Must set `visualize` true before running plot board!")

        self.ax.clear()
        self.ax.set_xticks(np.arange(self.size.cols))
        self.ax.set_yticks(np.arange(self.size.rows))
        self.ax.set_xlim(0, self.size.cols)
        self.ax.set_ylim(0, self.size.rows)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        # Create a checkerboard pattern
        for i in range(self.size.rows):
            for j in range(self.size.cols):
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

        # Draw the gradient colored path
        for i in range(len(self.path) - 1):
            x1, y1 = self.path[i]
            x2, y2 = self.path[i + 1]

            color = plt.cm.coolwarm(i / (self.size.rows * self.size.cols - 1))  # type: ignore[attr-defined]

            self.ax.plot(
                [y1 + 0.5, y2 + 0.5],
                [x1 + 0.5, x2 + 0.5],
                color=color,
                marker="o",
            )

        # Flip board to move 0,0 to top right corner
        plt.gca().invert_yaxis()
        plt.draw()
        plt.pause(0.01)

    def close(self) -> None:
        """
        Turn off the visualization.
        """
        # Turn off interactive mode
        if self.visualize:
            plt.ioff()
            plt.show()
