# Tic Tac Toe (Python)

A simple console Tic Tac Toe game written in plain Python — a classic minor
project. No external libraries needed.

## Features

- **Two-player mode** — two people play on the same keyboard.
- **Vs computer** — two difficulty levels:
  - *Easy*: the computer picks random empty cells.
  - *Hard*: unbeatable AI using the **minimax** algorithm.
- Input validation (rejects letters, out-of-range numbers and taken cells).
- Win / draw detection, replay option and a running score board.
- Unit tests included.

## Requirements

Python 3.8 or newer. Only the standard library is used.

## How to run

```bash
python tic_tac_toe.py
```

You will see a menu:

```
Select a mode:
  1. Two players (same keyboard)
  2. Play against the computer
  3. Quit
```

The board shows numbers 1-9 for the empty cells:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Type the number of the cell you want to claim. `X` always moves first.

## How to run the tests

```bash
python -m unittest -v
```

## Project structure

```
tic_tac_toe/
├── tic_tac_toe.py       # the game (board, rules, AI, menu)
├── test_tic_tac_toe.py  # unit tests
├── README.md
└── .gitignore
```

## How it works

| Function | Purpose |
|---|---|
| `create_board()` | returns a list of 9 empty cells |
| `print_board(board)` | draws the 3x3 grid |
| `available_moves(board)` | lists the empty cells |
| `winner(board)` | returns `'X'`, `'O'`, `'draw'` or `None` |
| `minimax(board, player)` | scores a position assuming perfect play |
| `best_move(board)` | picks the highest-scoring move for the AI |
| `play_round(mode)` | plays one full round |
| `main()` | menu, score keeping and replay loop |

The board is a flat list of 9 strings. The eight winning lines are stored in
`WIN_LINES`, so a win is just a check of those triples.

## Ideas to extend it

- Add a graphical version with `tkinter`.
- Add a 4x4 board with four-in-a-row.
- Save the score to a file so it survives restarts.
- Add an alpha-beta pruning version of minimax and compare speed.

## License

MIT — free to use for college projects and learning.
