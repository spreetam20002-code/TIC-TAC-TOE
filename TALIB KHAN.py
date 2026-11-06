"""
Tic Tac Toe - console game (minor project)

Features
--------
* Human vs Human
* Human vs Computer (Easy = random moves, Hard = unbeatable minimax)
* Input validation, replay, running score board
* Pure standard library - nothing to install

Run:
    TALIB KHAN.py
"""

import random

# The 8 winning lines (indexes of the 3x3 board)
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
)

HUMAN = "X"
COMPUTER = "O"


# ----------------------------------------------------------------------
# Board helpers
# ----------------------------------------------------------------------
def create_board():
    """Return a fresh, empty board (9 empty cells)."""
    return [" " for _ in range(9)]


def print_board(board):
    """Print the board with position numbers for the empty cells."""
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def available_moves(board):
    """Return the list of empty cell indexes."""
    return [i for i, value in enumerate(board) if value == " "]


def winner(board):
    """
    Return 'X' or 'O' if that player has won, 'draw' if the board is full,
    otherwise None.
    """
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None


def is_game_over(board):
    return winner(board) is not None


# ----------------------------------------------------------------------
# Computer player
# ----------------------------------------------------------------------
def random_move(board):
    """Easy level: pick any empty cell."""
    return random.choice(available_moves(board))


def minimax(board, player, depth=0):
    """
    Hard level: return the best score for `player` assuming both sides
    play perfectly. The depth is subtracted so the AI prefers to win as
    quickly as possible (and to lose as late as possible).
    """
    result = winner(board)
    if result == COMPUTER:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if result == "draw":
        return 0

    opponent = HUMAN if player == COMPUTER else COMPUTER
    scores = []
    for move in available_moves(board):
        board[move] = player
        scores.append(minimax(board, opponent, depth + 1))
        board[move] = " "

    return max(scores) if player == COMPUTER else min(scores)


# Order in which the AI considers cells: centre first, then corners,
# then edges. Used only to break ties, so the play looks natural.
PREFERRED_ORDER = (4, 0, 2, 6, 8, 1, 3, 5, 7)


def best_move(board):
    """Hard level: return the cell with the highest minimax score."""
    best_score = -100
    best_cell = None
    for move in PREFERRED_ORDER:
        if board[move] != " ":
            continue
        board[move] = COMPUTER
        score = minimax(board, HUMAN, 1)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_cell = move
    return best_cell


# ----------------------------------------------------------------------
# Human input
# ----------------------------------------------------------------------
def get_human_move(board, player):
    """Keep asking until the player enters a valid, empty cell (1-9)."""
    while True:
        raw = input(f"Player {player}, choose a cell (1-9): ").strip()

        if not raw.isdigit():
            print("  ! Please type a number from 1 to 9.")
            continue

        position = int(raw)
        if not 1 <= position <= 9:
            print("  ! That number is out of range. Use 1 to 9.")
            continue

        index = position - 1
        if board[index] != " ":
            print("  ! That cell is already taken. Pick another one.")
            continue

        return index


# ----------------------------------------------------------------------
# Game modes
# ----------------------------------------------------------------------
def play_round(mode):
    """
    Play one round. `mode` is '1' (two players) or '2' (vs computer).
    Returns 'X', 'O' or 'draw'.
    """
    board = create_board()
    difficulty = None

    if mode == "2":
        print("Choose difficulty: 1 = Easy, 2 = Hard (unbeatable)")
        difficulty = input("Your choice (1/2): ").strip()
        if difficulty not in ("1", "2"):
            difficulty = "1"

    current = HUMAN  # X always starts
    while True:
        print_board(board)

        if mode == "2" and current == COMPUTER:
            print("Computer is thinking...")
            move = random_move(board) if difficulty == "1" else best_move(board)
        else:
            move = get_human_move(board, current)

        board[move] = current
        result = winner(board)

        if result is not None:
            print_board(board)
            if result == "draw":
                print("It's a draw!")
            elif mode == "2" and result == COMPUTER:
                print("Computer wins!")
            else:
                print(f"Player {result} wins!")
            return result

        current = COMPUTER if current == HUMAN else HUMAN


def main():
    print("=" * 40)
    print("        TIC TAC TOE")
    print("=" * 40)

    scores = {"X": 0, "O": 0, "draw": 0}

    while True:
        print("\nSelect a mode:")
        print("  1. Two players (same keyboard)")
        print("  2. Play against the computer")
        print("  3. Quit")

        mode = input("Enter 1, 2 or 3: ").strip()

        if mode == "3":
            break
        if mode not in ("1", "2"):
            print("  ! Invalid choice, please try again.")
            continue

        result = play_round(mode)
        scores[result] += 1

        print(f"\nScore  ->  X: {scores['X']}   "
              f"O: {scores['O']}   Draws: {scores['draw']}")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThanks for playing. Final score:")
    print(f"  X: {scores['X']}   O: {scores['O']}   Draws: {scores['draw']}")
    print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame interrupted. Bye!")
