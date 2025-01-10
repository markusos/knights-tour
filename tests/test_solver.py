from src.tour.solver import KnightTourSolver


def test_solve_knight_tour():
    A, B = 5, 5
    start_x, start_y = 0, 0
    KnightTourSolver((A, B), (start_x, start_y), False)
