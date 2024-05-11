#!/usr/bin/env python3

import random

# Constant variables.
NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 5

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def randomize_operator():
    """
    Randomly selects an arithmetic operator (+, -, or *).

    Returns:
        str: the selected operator as a string.
    """
    operator = random.randint(0, 2)

    if operator == 0:
        operator_str = "+"
    elif operator == 1:
        operator_str = "-"
    else:
        operator_str = "*"

    return operator_str


def generate_random_arithmetic_question():
    """
    Generates a random arithmetic question and prompts the user to solve it.

    Returns:
        bool: `True` if the user's answer is correct, `False` otherwise.
    """
    while True:
        a = random.randint(NB_MIN, NB_MAX)
        b = random.randint(NB_MIN, NB_MAX)

        operator = randomize_operator()

        number_str = input(f"Calculate: {a} {operator} {b} = ")
        try:
            number_int = int(number_str)
        except ValueError:
            print(f"{RED}ERROR: please enter a valid number.{RESET}")
            continue

        if operator == "+":
            answer = a + b
        elif operator == "-":
            answer = a - b
        elif operator == "*":
            answer = a * b

        if number_int == answer:
            return True

        return False


def main():
    """
    Main function that runs the arithmetic quiz game.
    """
    # Print initial instructions.
    print(f"\n{YELLOW}Try to solve as many arithmetic questions as you can out of {NB_QUESTIONS} total.{RESET}\n")

    nb_points = 0

    # Main game loop.
    for i in range(0, NB_QUESTIONS):

        print(f"Question {YELLOW}{i + 1}{RESET} on {YELLOW}{NB_QUESTIONS}{RESET}:")
        if generate_random_arithmetic_question():
            print(f"{GREEN}Good answer!{RESET}\n")
            nb_points += 1
        else:
            print(f"{MAGENTA}Wrong answer!{RESET}\n")

    # Calculate average and percentage.
    average = int(NB_QUESTIONS/2)
    percentage = int((nb_points / NB_QUESTIONS) * 100)

    # Print final results.
    print(f"Your score is {nb_points} out of {NB_QUESTIONS} ({percentage}%).")

    # Provide feedback based on performance.
    if nb_points == NB_QUESTIONS:
        print(f"{BLUE}Perfect!{RESET}\n")
    elif nb_points > average:
        print(f"{BLUE}Good level!{RESET}\n")
    elif nb_points == 0:
        print(f"{BLUE}You need to brush up on your maths...{RESET}\n")
    else:
        print(f"{BLUE}You can do better.{RESET}\n")

    # Thank the player for playing.
    print(f"{YELLOW}Thanks for playing!{RESET}\n")


if __name__ == "__main__":
    main()
