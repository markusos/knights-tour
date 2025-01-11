from src.knights_tour.knights_tour_solver import KnightsTourSolver


def test_knights_tour_solve_knight_tour():
    size = (5, 5)
    start = (2, 2)
    solver = KnightsTourSolver(size, start)
    solver.solve()

    # Start position is still set to 0
    assert solver.board[start[0]][start[1]] == 0
    # Board is filled with moves
    assert all(cell != -1 for row in solver.board for cell in row)


def test_knights_tour_no_solution():
    size = (4, 4)
    start = (0, 0)
    solver = KnightsTourSolver(size, start)
    solver.solve()

    # Start position is still set to 0
    assert solver.board[start[0]][start[1]] == 0
    # Board has at least one incompleated position
    assert any(cell == -1 for row in solver.board for cell in row)


def test_knights_tour_solve_knight_tour_with_loop():
    size = (8, 8)
    start = (4, 4)
    solver = KnightsTourSolver(size, start, loop=True)
    solver.solve()

    # Last move is back to start
    assert solver.board[start[0]][start[1]] == 64
    # Board is filled with moves
    assert all(cell != -1 for row in solver.board for cell in row)
