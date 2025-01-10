import pytest
from src.tour.knight import solve_knight_tour


def test_solve_knight_tour():
    A, B = 5, 5
    start_x, start_y = 0, 0
    solve_knight_tour(A, B, start_x, start_y, visualize=False)
