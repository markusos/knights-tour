import matplotlib.pyplot as plt
import numpy as np
import argparse


def is_valid_move(x, y, board, A, B):
    return 0 <= x < A and 0 <= y < B and board[x][y] == -1


def print_board(board):
    for row in board:
        print(" ".join(str(cell).rjust(2, "0") for cell in row))
    print()


def plot_board(ax, board, path_x, path_y, A, B):
    ax.clear()
    ax.set_xticks(np.arange(B))
    ax.set_yticks(np.arange(A))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)

    # Create a checkerboard pattern
    for i in range(A):
        for j in range(B):
            color = "white" if (i + j) % 2 == 0 else "gray"
            ax.add_patch(
                plt.Rectangle(
                    (j, i), 1, 1, linewidth=2, edgecolor="black", facecolor=color
                )
            )
            # Add the move number to the cell
            if board[i][j] != -1:
                ax.text(
                    j + 0.5,
                    i + 0.5,
                    str(board[i][j]).rjust(2, "0"),
                    ha="center",
                    va="center",
                    color="black",
                )

    # Create a gradient color for the path
    for i in range(len(path_x) - 1):
        ax.plot(
            path_x[i : i + 2],
            path_y[i : i + 2],
            color=plt.cm.coolwarm(i / (A * B - 1)),
            marker="o",
        )

    plt.gca().invert_yaxis()
    plt.draw()
    plt.pause(0.1)


def get_degree(x, y, board, moves, A, B):
    count = 0
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(next_x, next_y, board, A, B):
            count += 1
    return count


def solve_knight_tour(A, B, start_x, start_y, visualize):
    # Initialize the chessboard
    board = [[-1 for _ in range(B)] for _ in range(A)]

    # Possible moves for a knight
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board[start_x][start_y] = 0

    path_x = [start_y + 0.5]
    path_y = [start_x + 0.5]

    fig, ax = plt.subplots() if visualize else (None, None)

    def solve(x, y, move_count):
        if move_count == A * B:
            return True

        # Sort moves based on Warnsdorff's rule
        next_moves = sorted(
            moves,
            key=lambda move: get_degree(x + move[0], y + move[1], board, moves, A, B),
        )

        for move in next_moves:
            next_x, next_y = x + move[0], y + move[1]
            if is_valid_move(next_x, next_y, board, A, B):
                board[next_x][next_y] = move_count
                path_x.append(next_y + 0.5)
                path_y.append(next_x + 0.5)

                # Update the plot if visualization is enabled
                if visualize:
                    plot_board(ax, board, path_x, path_y, A, B)

                if solve(next_x, next_y, move_count + 1):
                    return True

                # Backtrack
                board[next_x][next_y] = -1
                path_x.pop()
                path_y.pop()

                # Update the plot if visualization is enabled
                if visualize:
                    plot_board(ax, board, path_x, path_y, A, B)

        return False

    if solve(start_x, start_y, 1):
        print_board(board)
        if visualize:
            plot_board(ax, board, path_x, path_y, A, B)
    else:
        print("No solution found")


def main():
    parser = argparse.ArgumentParser(description="Solve the Knight's Tour problem.")
    parser.add_argument(
        "--size",
        type=int,
        nargs=2,
        default=(8, 8),
        metavar=("a", "b"),
        help="Size of the board (a, b), (default: 8, 8)",
    )
    parser.add_argument(
        "--start",
        type=int,
        nargs=2,
        default=(0, 0),
        metavar=("x", "y"),
        help="Knight's starting coordinates (x, y), (default: 0, 0)",
    )
    parser.add_argument(
        "-v",
        "--visualize",
        action="store_true",
        help="Enable visualization of the knight's tour",
    )

    args = parser.parse_args()

    plt.ion()  # Turn on interactive mode if visualization is enabled
    solve_knight_tour(
        args.size[0], args.size[1], args.start[0], args.start[1], args.visualize
    )
    if args.visualize:
        plt.ioff()  # Turn off interactive mode
        plt.show()


if __name__ == "__main__":
    main()
