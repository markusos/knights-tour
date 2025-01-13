from src.knights_tour.board import Board, Position, BoardSize


def test_board():
    size = BoardSize(5, 4)
    pos = Position(2, 2)
    board = Board(size)

    # Test size
    assert board.size.rows == 5
    assert board.size.cols == 4

    # Test set
    board.set(pos, 5)

    assert board.get(pos) == 5
    assert pos in board.path

    # Test unset
    board.unset(pos)

    assert board.get(pos) == -1
    assert pos not in board.path
