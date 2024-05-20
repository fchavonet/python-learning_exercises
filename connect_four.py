#!/usr/bin/env python3

import os
import time

# Constant variables.
ROWS = 6
COLS = 7

PLAYER_ONE = "🟡"
PLAYER_TWO = "🔴"

EMPTY = "⚪"

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def clear_screen():
    """
    Clears the console screen.
    """
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")


def print_instructions():
    """
    Prints the game instructions.
    """
    print(f"\n{YELLOW}Welcome to this 2-player Connect Four game!")
    print(f"To win, connect four of your pieces in a row, column, or diagonal.{RESET}\n")


def create_board():
    """
    Creates a new empty game board.

    Returns:
        list: a 2D list representing the game board.
    """
    board = []
    for _ in range(ROWS):
        board.append([EMPTY] * COLS)
    return board


def print_board(board):
    """
    Prints the current state of the game board.

    Args:
        board (list): a 2D list representing the game board.
    """
    print(f"    {'     '.join(str(i + 1) for i in range(COLS))}")
    print(f"{BLUE} +{'-----+' * COLS}{RESET}")

    for row in board:
        print(f"{BLUE} | {'  | '.join(row)}  |")
        print(f" +{'-----+' * COLS}{RESET}")

    print()


def is_valid_column(board, col):
    """
    Checks if a column is valid for placing a piece.

    Args:
        board (list): a 2D list representing the game board.
        col (int): the column index to check.

    Returns:
        bool: True if the column is valid, False otherwise.
    """
    return board[0][col] == EMPTY


def get_next_open_row(board, col):
    """
    Finds the next available row in a column for placing a piece.

    Args:
        board (list): a 2D list representing the game board.
        col (int): the column index to check.

    Returns:
        int: the row index where the piece can be placed.
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row


def drop_piece(board, col, piece):
    """
    Animates the piece falling and places it on the game board.

    Args:
        board (list): a 2D list representing the game board.
        col (int): the column index where the piece will be placed.
        piece (str): the piece to place on the board.
    """
    row = get_next_open_row(board, col)

    for i in range(row + 1):
        if i > 0:
            board[i - 1][col] = EMPTY

        board[i][col] = piece

        clear_screen()
        print_instructions()
        print_board(board)

        time.sleep(0.1)

    board[row][col] = piece


def winning_move(board, piece):
    """
    Checks if the current player has won the game.

    Args:
        board (list): a 2D list representing the game board.
        piece (str): the player's piece ("🟡" or "🔴").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal locations for a win
    for col in range(COLS - 3):
        for row in range(ROWS):
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
                return True

    # Check vertical locations for a win
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and board[row + 3][col] == piece:
                return True

    # Check positively sloped diagonals
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col+3] == piece:
                return True

    return False


def get_valid_column():
    """
    Asks the player to choose a valid column to place their piece.

    Returns:
        int: the index of the chosen column.
    """
    while True:
        try:
            col = int(input(f"Choose a column (1-{COLS}): "))
            col -= 1
            if 0 <= col < COLS:
                return col
            else:
                print(f"Invalid input. Please enter a number between 1 and {COLS}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def is_full(board):
    """
    Checks if the game board is full.

    Args:
        board (list): a 2D list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for col in range(COLS):
        if is_valid_column(board, col):
            return False
    return True


def main():
    """
    Main function that executes the Connect Four game.
    """
    clear_screen()

    # Print initial instructions.
    print_instructions()

    # Initialize the game board.
    board = create_board()
    print_board(board)

    # Initialize the turn counter.
    turn = 0

    # Main game loop.
    while True:
        # Determine the current player.
        if turn == 0:
            print(f"{GREEN}PLAYER 1: 🟡{RESET}")
        else:
            print(f"{GREEN}PLAYER 2: 🔴{RESET}")

        # Ask the current player to choose a column.
        col = get_valid_column()

        # If the chosen column is valid, proceed with the move.
        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            if turn == 0:
                drop_piece(board, col, PLAYER_ONE)
                if winning_move(board, PLAYER_ONE):
                    # If the current player wins, end the game.
                    clear_screen()
                    print_instructions()
                    print_board(board)
                    print(f"{GREEN}🟡 - Player 1 WINS!{RESET}\n")
                    print(f"{YELLOW}Thanks for playing.{RESET}\n")
                    break
            else:
                drop_piece(board, col, PLAYER_TWO)
                if winning_move(board, PLAYER_TWO):
                    # If the current player wins, end the game.
                    clear_screen()
                    print_instructions()
                    print_board(board)
                    print(f"{GREEN}🔴 - Player 2 WINS!{RESET}\n")
                    print(f"{YELLOW}Thanks for playing.{RESET}\n")
                    break

            # Update the game state and print the updated board.
            clear_screen()
            print_instructions()
            print_board(board)

            # Check for a tie game.
            if is_full(board):
                print(f"{GREEN}It's a tie!{RESET}")
                print(f"{YELLOW}Thanks for playing.{RESET}\n")
                break

            # Switch to the next player's turn.
            turn += 1
            turn = turn % 2
        else:
            # If the chosen column is full, prompt the player to choose another column.
            print(f"\n{MAGENTA}This column is full, please choose another one.{RESET}\n")


if __name__ == "__main__":
    main()
