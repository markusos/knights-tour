import numpy as np
import matplotlib.pyplot as plt


class KnightTourSolver:
    # Possible moves for a knight
    MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def __init__(self, size, start, visualize):
        self.A = size[0]
        self.B = size[1]

        # Initialize the chessboard
        self.board = [[-1 for _ in range(self.B)] for _ in range(self.A)]

        self.start_x = start[0]
        self.start_y = start[1]

        # Place the knight at the starting position
        self.board[self.start_x][self.start_y] = 0
        self.path_x = [self.start_y + 0.5]
        self.path_y = [self.start_x + 0.5]

        self.visualize = visualize
        self.fig, self.ax = plt.subplots() if self.visualize else (None, None)

    def solve(self):
        plt.ion()  # Turn on interactive mode if visualization is enabled

        if self.__solve_knight_tour(self.start_x, self.start_y, 1):
            self.__print_board()
        else:
            print("No solution found")

        # Turn off interactive mode
        if self.visualize:
            plt.ioff()
            plt.show()

    def __is_valid_move(self, x, y):
        return 0 <= x < self.A and 0 <= y < self.B and self.board[x][y] == -1

    def __print_board(self):
        for row in self.board:
            print(" ".join(str(cell).rjust(2, "0") for cell in row))
        print()

    def __plot_board(self):
        self.ax.clear()
        self.ax.set_xticks(np.arange(self.B))
        self.ax.set_yticks(np.arange(self.A))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(True)

        # Create a checkerboard pattern
        for i in range(self.A):
            for j in range(self.B):
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
                color=plt.cm.coolwarm(i / (self.A * self.B - 1)),
                marker="o",
            )

        plt.gca().invert_yaxis()
        plt.draw()
        plt.pause(0.01)

    def __get_degree(self, x, y):
        count = 0
        for move in self.MOVES:
            next_x, next_y = x + move[0], y + move[1]
            if self.__is_valid_move(next_x, next_y):
                count += 1
        return count

    def __solve_knight_tour(self, x, y, move_count):
        if move_count == self.A * self.B:
            return True

        # Sort moves based on Warnsdorff's rule
        next_moves = sorted(
            self.MOVES,
            key=lambda move: self.__get_degree(x + move[0], y + move[1]),
        )

        for move in next_moves:
            next_x, next_y = x + move[0], y + move[1]

            if self.__is_valid_move(next_x, next_y):
                self.board[next_x][next_y] = move_count
                self.path_x.append(next_y + 0.5)
                self.path_y.append(next_x + 0.5)

                # Update the plot if visualization is enabled
                if self.visualize:
                    self.__plot_board()

                if self.__solve_knight_tour(next_x, next_y, move_count + 1):
                    return True

                # Backtrack
                self.board[next_x][next_y] = -1
                self.path_x.pop()
                self.path_y.pop()

                # Update the plot if visualization is enabled
                if self.visualize:
                    self.__plot_board()

        return False
