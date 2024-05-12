#!/usr/bin/env python3

import requests

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def get_valid_amount():
    """
    Ask the user to input an amount to convert.

    Returns:
        float: the valid amount entered by the user.
    """
    while True:
        amount = input("Enter amount to convert: ")

        try:
            amount = float(amount)
            return amount

        except ValueError:
            print(f"{RED}Error: please enter a valid amount.{RESET}")


def get_valid_currency(message):
    """
    Ask the user to input a currency code and validate it using an API.

    Args:
        message (str): the message to prompt the user for input.

    Returns:
        str: the valid currency code entered by the user.
    """
    while True:
        currency = input(message).upper()

        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
            data = response.json()

            if "rates" in data:
                return currency
            else:
                print(f"{RED}Error: please enter a valid currency.{RESET}")

        except Exception as e:
            print(f"{RED}Error: please enter a valid currency.{RESET}")


def convert_currency(amount, base_currency, target_currency):
    """
    Convert an amount from one currency to another using an API.

    Args:
        amount (float): the amount to convert.
        base_currency (str): the currency code of the amount.
        target_currency (str): the currency code to convert the amount to.

    Returns:
        float or None: the converted amount if successful, otherwise None.
    """
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()

        if target_currency in data["rates"]:
            exchange_rate = data["rates"][target_currency]
            converted_amount = amount * exchange_rate
            return converted_amount

    except Exception:
        print(f"{RED}a tapper !{RESET}")
        return None
    
def print_top_currencies():
    """
    Print a list of top 5 currencies along with their currency codes.
    """
    top_currencies = [
        ("US Dollar", "USD"),
        ("Euro", "EUR"),
        ("Japanese Yen", "JPY"),
        ("British Pound", "GBP"),
        ("Australian Dollar", "AUD")
    ]

    print(f"{BLUE}=" * 25)
    for currency in top_currencies:
        print(f"|{currency[0]:<20}{currency[1]:<3}|")
    print("=" * 25)
    print(f"{RESET}")


def main():
    """
    Main function that executes the currency conversion program.
    """
    # Print initial instructions.
    print(f"\n{YELLOW}Try to convert an amount!{RESET}\n")
    print_top_currencies()

    # Get user input.
    amount = get_valid_amount()
    base_currency = get_valid_currency("Base currency: ")
    target_currency = get_valid_currency("Target currency: ")

    # Convert currency and display result.
    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"\n{YELLOW}{amount:.2f}{RESET} {GREEN}{base_currency}{RESET} is worth {YELLOW}{converted_amount:.2f}{RESET} {GREEN}{target_currency}{RESET}\n")


if __name__ == "__main__":
    main()
