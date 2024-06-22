#!/usr/bin/env python3

import json
import requests

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def main():
    """
    Main function to search for a LEGO® set using the Brickset API.

    Raises:
        ValueError: if the API key is not found in the configuration file.
    """
    # Load API key from the configuration file.
    with open("./config.json") as config_file:
        config = json.load(config_file)
        api_key = config.get("api_key")

    if not api_key:
        raise ValueError(f"{RED}Error: API key not found in the configuration file.{RESET}")

    print(f"\n{YELLOW}BRICKSET FINDER")
    print("=" * 15)

    # Get the LEGO set number from user input.
    set_number = input(f"{RESET}\nEnter the LEGO® set number: {BLUE}")
    print("")

    # API request setup
    method = "getSets"
    url = f"https://brickset.com/api/v3.asmx/{method}"

    request_data = {
        "apiKey": api_key,
        "userHash": "",
        "params": json.dumps({"query": set_number})
    }

    def clean_value(value):
        """
        Clean curly braces from a string.

        Args:
            value (str): the string value to clean.

        Returns:
            str: the cleaned string with curly braces removed.
        """
        if isinstance(value, str):
            return value.replace("{", "").replace("}", "")
        return value

    # Send the request
    response = requests.post(url, data=request_data)

    # Process the response
    if response.status_code == 200:
        data = response.json()
        if data["matches"] > 0:
            found_exact_match = False
            for set_info in data["sets"]:
                if set_info.get("number") == set_number:
                    found_exact_match = True
                    set_name = clean_value(set_info.get("name", "N/A"))
                    set_theme = clean_value(set_info.get("theme", "N/A"))
                    set_subtheme = clean_value(set_info.get("subtheme", "N/A"))
                    set_year = clean_value(set_info.get("year", "N/A"))
                    set_pieces = clean_value(set_info.get("pieces", "N/A"))
                    set_minifigs = clean_value(set_info.get("minifigs", "N/A"))
                    set_packagingType = clean_value(set_info.get("packagingType", "N/A"))

                    print(f"{MAGENTA}Name: {RESET}{set_name}")
                    print(f"{MAGENTA}Theme: {RESET}{set_theme}")
                    print(f"{MAGENTA}Subtheme: {RESET}{set_subtheme}")
                    print(f"{MAGENTA}Year: {RESET}{set_year}")
                    print(f"{MAGENTA}Pieces: {RESET}{set_pieces}")
                    print(f"{MAGENTA}Minifigures: {RESET}{set_minifigs}")
                    print(f"{MAGENTA}Packaging: {RESET}{set_packagingType}")

            if not found_exact_match:
                print(f"{RED}No exact match found.{RESET}")
        else:
            print(f"{RED}No sets found.{RESET}")
    else:
        print(f"{RED}Error: {response.status_code}{RESET}")
        print(response.text)

    print("")


if __name__ == "__main__":
    main()
