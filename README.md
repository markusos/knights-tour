# Knight's Tour Solver

This script attempts provides a solution to the Knight's Tour problem using Warnsdorff's Rule. The Knight's Tour problem involves moving a knight on a chessboard such that the knight visits every square exactly once.

## Features

- Attempts to solves the [Knight's Tour problem](https://en.wikipedia.org/wiki/Knight%27s_tour) for any \( A x B \) board size.
- Allows specifying the starting position of the knight.
- Optional real-time visualization of the knight's path using `matplotlib`.

## Requirements

- Python 3.9
- `matplotlib` library

```sh
uv run knight.py
```

## Usage
The script can be run from the command line with various options:

### Arguments
--rows: Number of rows in the board (default: 8)
--cols: Number of columns in the board (default: 8)
--start_x: Knight's starting x position (default: 0)
--start_y: Knight's starting y position (default: 0)
--visualize: Enable visualization of the knight's tour (optional)

### Examples
Solve the Knight's Tour problem on an 8x8 board starting at position (0,0) without visualization:

```
uv run knight.py --rows 8 --cols 8 --start_x 0 --start_y 0
```

Solve the Knight's Tour problem on a 5x5 board starting at position (2,2) with visualization:

```
uv run knight.py --rows 5 --cols 5 --start_x 2 --start_y 2 --visualize
```

## Implementation Details
The solution uses Warnsdorff's Rule, which is a heuristic-based approach. The algorithm selects the next move based on the accessibility of the squares, i.e., it always moves to the square with the fewest onward moves.

### Functions

`is_valid_move(x, y, board, A, B)`: Checks if a move is valid within the board boundaries and if the square has not been visited.

`print_board(board)`: Prints the board in a readable format.

`plot_board(ax, board, path_x, path_y, A, B)`: Plots the board and the knight's path using matplotlib.

`get_degree(x, y, board, moves, A, B)`: Calculates the number of valid moves from a given position.

`solve_knight_tour(A, B, start_x, start_y, visualize)`: Solves the Knight's Tour problem using Warnsdorff's Rule and optionally visualizes the solution.

## License

The MIT License (MIT)

Copyright (c) 2025 Markus Östberg

