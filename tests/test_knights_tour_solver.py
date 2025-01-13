import numpy as np

from src.knights_tour.knights_tour_solver import KnightsTourSolver
from src.knights_tour.board import Position


def test_knights_tour_solve_knight_tour():
    size = (5, 5)
    start = (2, 2)
    solver = KnightsTourSolver(size, start)
    solver.solve()

    # Start position is still set to 0
    assert solver.board.get(Position(*start)) == 0
    # Board is filled with moves
    assert all(cell != -1 for row in solver.board.rows() for cell in row)


def test_knights_tour_no_solution():
    size = (4, 4)
    start = (0, 0)
    solver = KnightsTourSolver(size, start)
    solver.solve()

    # Start position is still set to 0
    assert solver.board.get(Position(*start)) == 0
    # Board has at least one incompleated position
    assert any(cell == -1 for row in solver.board.rows() for cell in row)


def test_knights_tour_solve_knight_tour_with_loop():
    size = (8, 8)
    start = (4, 4)
    solver = KnightsTourSolver(size, start, loop=True)
    solver.solve()

    # Last move is back to start
    assert solver.board.get(Position(*start)) == 64

    # Board is filled with moves
    assert all(cell != -1 for row in solver.board.rows() for cell in row)

    # Assert expeceted board state
    expected = np.array(
        [
            [14, 11, 16, 35, 6, 9, 26, 31],
            [17, 34, 13, 10, 27, 32, 5, 8],
            [12, 15, 42, 33, 36, 7, 30, 25],
            [43, 18, 63, 56, 41, 28, 37, 4],
            [62, 57, 44, 53, 64, 55, 24, 29],
            [19, 52, 61, 58, 47, 40, 3, 38],
            [60, 45, 50, 21, 54, 1, 48, 23],
            [51, 20, 59, 46, 49, 22, 39, 2],
        ]
    )

    actual = np.array([row for row in solver.board.rows()])

    np.testing.assert_array_equal(actual, expected)
