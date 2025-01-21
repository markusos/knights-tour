import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes
from typing import Optional

from src.knights_tour.board import Board, Position


class BoardVisualizer:
    def __init__(
        self,
        visualize: bool = False,
    ):
        """
        Initializes the BoardVisualizer.

        Args:
            visualize (bool): Whether to plot the board state live.
        """
        self.visualize = visualize
        self.fig: Optional[Figure] = None
        self.ax: Optional[Axes] = None

        if self.visualize:
            self.fig, self.ax = plt.subplots()
            plt.ion()

    def print_board(self, board: Board) -> None:
        """
        Prints the board state.
        """
        max_num = board.size.rows * board.size.cols - 1
        width = len(str(max_num))
        for row in board.rows():
            print(" ".join(str(cell).rjust(width, "0") for cell in row))
        print()

    def plot_board(self, board: Board) -> None:
        """
        Plots the board state using matplotlib.
        """
        if not self.visualize:
            return None

        if self.ax is None:
            raise RuntimeError("Must set `visualize` true before running plot board!")

        self.ax.clear()
        self.ax.set_xticks(np.arange(board.size.cols))
        self.ax.set_yticks(np.arange(board.size.rows))
        self.ax.set_xlim(0, board.size.cols)
        self.ax.set_ylim(0, board.size.rows)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        # Create a checkerboard pattern
        for i in range(board.size.rows):
            for j in range(board.size.cols):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.ax.add_patch(
                    plt.Rectangle(
                        (j, i), 1, 1, linewidth=2, edgecolor="black", facecolor=color
                    )
                )
                # Add the move number to the cell
                value = board.get(Position(i, j))
                if value != -1:
                    self.ax.text(
                        j + 0.5,
                        i + 0.5,
                        str(value).rjust(2, "0"),
                        ha="center",
                        va="center",
                        color="black",
                    )

        # Draw the gradient colored path
        for i in range(len(board.path) - 1):
            x1, y1 = board.path[i]
            x2, y2 = board.path[i + 1]

            color = plt.cm.coolwarm(i / (board.size.rows * board.size.cols - 1))  # type: ignore[attr-defined]

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
        Turn off the visualization mode.
        """
        # Turn off interactive mode
        if self.visualize:
            plt.ioff()
            plt.show()
