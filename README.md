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

`--size`: Size of the board (a, b) (default: 8, 8)

`--start`: Knight's starting position (x, y) (default: 0, 0)

`--visualize`: Enable visualization of the knight's tour (optional)

### Examples
Solve the Knight's Tour problem on an 8x8 board starting at position (0,0) without visualization:

```
uv run knight.py --size 8 8 --start 0 0
```

Solve the Knight's Tour problem on a 5x5 board starting at position (2,2) with visualization:

```
uv run knight.py --size 5 5 --start 2 2 --visualize
```

## Implementation Details
The solution uses Warnsdorff's Rule, which is a heuristic-based approach. The algorithm selects the next move based on the accessibility of the squares, i.e., it always moves to the square with the fewest onward moves.

## License

The MIT License (MIT)

Copyright (c) 2025 Markus Östberg

