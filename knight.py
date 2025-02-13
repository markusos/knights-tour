import argparse
from src.knights_tour.knights_tour_solver import KnightsTourSolver


def main():
    parser = argparse.ArgumentParser(description="Solve the Knight's Tour problem.")
    parser.add_argument(
        "--size",
        type=int,
        nargs=2,
        default=(8, 8),
        metavar=("rows", "cols"),
        help="Size of the board (rows, cols), (default: 8, 8)",
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
    parser.add_argument(
        "-l",
        "--loop",
        action="store_true",
        help="Enable findng a closed knight's tour",
    )

    args = parser.parse_args()
    KnightsTourSolver(
        args.size, args.start, visualize=args.visualize, loop=args.loop
    ).solve()


if __name__ == "__main__":
    main()
