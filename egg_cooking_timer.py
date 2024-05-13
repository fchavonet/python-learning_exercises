#!/usr/bin/env python3

import time

# Constant variables.
UPDATE_INTERVAL = 30

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def program_selection():
    """
    Prompt the user to choose a program.

    Returns:
        str: the user's choice.
    """
    while True:
        user_choice = input("Choose a program: ")
        if user_choice in ["1", "2", "3"]:
            return user_choice
        print(f"{RED}ERROR: please enter a valid choice.{RESET}")


def cooking_time(user_choice):
    """
    Calculate the cooking time based on the user's choice.

    Args:
        user_choice (str): the user's selected program.

    Returns:
        int: the cooking time in seconds.
    """
    if user_choice == "1":
        print(f"\n{BLUE}You've selected the egg cooking timer for soft-boiled eggs, timer starts for 3 minutes.{RESET}\n")
        return 3 * 60
    elif user_choice == "2":
        print(f"\n{BLUE}You've selected the egg cooking timer for medium-boiled eggs, timer starts for 6 minutes.{RESET}\n")
        return 6 * 60
    elif user_choice == "3":
        print(f"\n{BLUE}You've selected the egg cooking timer for hard-boiled eggs, timer starts for 9 minutes.{RESET}\n")
        return 9 * 60


def print_remaining_time(duration):
    """
    Print the remaining time in minutes and seconds.

    Args:
        duration (int): the remaining time in seconds.
    """
    min = duration // 60
    sec = duration - min * 60
    print(f"{GREEN}{min:02d}:{sec:02d}{RESET}")


def main():
    """
    Main function that runs the egg timer program.
    """
    # Print initial instructions.
    print(f"\n{YELLOW}EGG COOKING TIMER")
    print(f"=" * 17)
    print(f"{RESET}")
    print("1 - Soft-boiled eggs (3 minutes)")
    print("2 - Medium-boiled eggs (6 minutes)")
    print("3 - Hard-boiled eggs (9 minutes)")

    # Prompt the user to select a program and get the cooking time.
    user_choice = program_selection()
    duration = cooking_time(user_choice)

    # Loop until the duration is finished.
    while duration > 0:
        # Wait for the update interval.
        for i in range(UPDATE_INTERVAL):
            print(f"{MAGENTA}.{RESET}", end="", flush=True)
            time.sleep(1)
            duration -= 1

        # Print remaining time.
        print("\nRemaining time:", end=" ")
        print_remaining_time(duration)

    # Print completion message.
    print(f"{YELLOW}\nCooking completed!{RESET}\n")


if __name__ == "__main__":
    main()
