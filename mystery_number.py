#!/usr/bin/env python3

import random

# Constant variables.
NB_MIN = 1
NB_MAX = 100
TOTAL_ATTEMPTS = 10

# Generate a random mystery number within the specified range.
MYSTERY_NUMBER = random.randint(NB_MIN, NB_MAX)

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def get_valid_attempt():
    """
    Get a valid attempt from the user.

    Returns:
        int: valid attempt entered by the user.
    """
    while True:
        number_str = input("Please enter your attempt: ")
        try:
            number_int = int(number_str)
            if NB_MIN - 1 < number_int < NB_MAX:
                return number_int
            else:
                print(f"{RED}ERROR: your attempt must be between {NB_MIN} and {NB_MAX}.{RESET}")
        except ValueError:
            print(f"{RED}ERROR: please enter a valid number.{RESET}")


# Print initial instructions for the game.
print(f"\n{YELLOW}Try to guess the Mystery Number between {NB_MIN} and {NB_MAX} within {TOTAL_ATTEMPTS} attempts.{RESET}\n")

# Main game loop.
for i in range(TOTAL_ATTEMPTS):
    attemps = TOTAL_ATTEMPTS - i
    nb_attemps = i + 1

    print(f"You have {YELLOW}{attemps}{RESET} attempts left out of {YELLOW}{TOTAL_ATTEMPTS}{RESET}.")
    number = get_valid_attempt()

    if number < MYSTERY_NUMBER:
        print(f"{BLUE}The mystery number is larger.{RESET}\n")
    elif number > MYSTERY_NUMBER:
        print(f"{BLUE}The mystery number is smaller.{RESET}\n")
    else:
        print(f"\n{GREEN}Congratulations!\nYou've guessed the mystery number in {nb_attemps} attempts!{RESET}\n")
        break

# Display a message if the player runs out of attempts.
if nb_attemps == TOTAL_ATTEMPTS:
    print(f"{MAGENTA}Sorry, you've run out of attempts.\nBetter luck next time!{RESET}\n")

# Thank the player for playing.
print(f"{YELLOW}Thanks for playing!{RESET}\n")
