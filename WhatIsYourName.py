# WhatIsYourName.py
"""
This script prompts the user for their first and last names,
then prints the full name in a formatted manner.
Author: Aquilas DJENONTIN
"""


def print_full_name(first_name, last_name):
    """Prints the full name by combining first and last names."""
    full_name = f"{first_name} {last_name}"
    print(full_name)


if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print_full_name(first_name, last_name)
