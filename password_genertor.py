#!/usr/bin/env python3

import pyperclip
import secrets
import string

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def generate_password():
    """
    Generates a random password.

    Returns:
        str: the generated password.
    """
    # Define the alphabet for generating the password.
    alphabet = string.ascii_letters + string.digits
    # Define the length and the number of segments in the password.
    segment_length = 6
    segments = 3

    # Initialize an empty list to store password segments.
    password_segments = []

    # Generate segments of the password.
    for _ in range(segments):
        segment = ""
        for _ in range(segment_length):
            segment += secrets.choice(alphabet)
        password_segments.append(segment)

    # Combine segments to form the password.
    password = "-".join(password_segments)

    return password


def main():
    """
    Main function that runs the password generator program.
    """
    print(f"\n{YELLOW}PASSWORD GENERATOR")
    print("=" * 18)

    while True:
        # Ask the user if they want to generate a new password.
        ask_to_generate = input(f"\n{RESET}Do you want to generate a new password ({GREEN}YES{RESET}/{RED}NO{RESET}): ").lower().strip()

        # Generate and copy a new password if the user chooses "YES".
        if ask_to_generate == "yes" or ask_to_generate == "y":
            generated_password = generate_password()
            pyperclip.copy(generated_password)
            print(f"\nPassword generated and copied to clipboard: {YELLOW}{generated_password}{RESET}")
        # Exit the program if the user chooses "NO".
        elif ask_to_generate == "no" or ask_to_generate == "n":
            print(f"\n{YELLOW}Thank you for using this simple password generator.{RESET}\n")
            break
        else:
            # Prompt the user to provide a valid input if their input is not recognized.
            print(f"{MAGENTA}Please answer with YES or NO.{RESET}")


if __name__ == "__main__":
    main()
