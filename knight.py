import argparse
from src.tour.solver import KnightTourSolver


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
    KnightTourSolver(args.size, args.start, args.visualize).solve()


if __name__ == "__main__":
    main()
