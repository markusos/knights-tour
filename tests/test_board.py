from src.knights_tour.board import Board, Position, BoardSize


def test_board():
    size = BoardSize(5, 4)
    pos = Position(2, 2)
    board = Board(size)

    # Test size
    assert board.size.rows == 5
    assert board.size.cols == 4

    # Test set
    board.set(pos)

    assert board.get(pos) == 0
    assert pos in board.path
    assert board.current_position() == pos

    # Test copy
    board_copy = board.copy()

    assert board_copy.size.rows == 5
    assert board_copy.size.cols == 4
    assert board_copy.get(pos) == 0

    board_copy.set(Position(1, 1))
    assert board.get(Position(1, 1)) == -1
    assert board_copy.get(Position(1, 1)) == 1
    assert board_copy.current_position() == Position(1, 1)
