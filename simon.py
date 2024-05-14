#!/usr/bin/env python3

import os
import random
import time

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
    Prints game instructions.
    """
    clear_screen()
    print(f"{YELLOW}Try to remember and repeat the number sequence correctly.{RESET}\n")
    print("Press ENTER to start...", end="")
    input()


def generate_random_sequence(length):
    """
    Generates a random number sequence of given length.

    Parameters:
    - length (int): the length of the sequence.

    Returns:
    - str: the generated random number sequence.
    """
    sequence = ""
    for i in range(length):
        sequence += str(random.randint(0, 9))
    return sequence


def print_sequence(sequence):
    """
    Prints the given number sequence.

    Parameters:
    - sequence (str): the number sequence to be printed.
    """
    print(f"{MAGENTA}Remember the sequence: {RESET}")
    print(sequence)


def main():
    """
    Main function that runs the Simon game
    """
    score = 0

    # Generate the first sequence of numbers.
    first_sequence_length = 4
    sequence = generate_random_sequence(first_sequence_length)

    # Print initial instructions.
    print_instructions()

    # Main game loop.
    while True:
        clear_screen()
        print_sequence(sequence)
        time.sleep(3)
        clear_screen()

        # Get user input.
        answer = input(f"{GREEN}What is the sequence: {RESET}\n")
        if answer == sequence:
            score += 1
            sequence += str(random.randint(0, 9))
        else:
            break

    # Game over.
    print(f"\n{RED}Game over!{RESET}\n")

    # Display final score.
    print(f"The sequence was {sequence}...")
    print(f"Your final score is: {YELLOW}{score}{RESET}\n")

    # Thank the player for playing.
    print(f"{YELLOW}Thanks for playing!{RESET}\n")


if __name__ == "__main__":
    main()
