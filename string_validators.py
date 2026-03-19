# StringValidators.py
"""
Docstring for StringValidators
This module contains a function to validate the presence of different character types in a string.
Function: string_validators
Parameters:
    s (str): The input string to validate.
Returns:
    tuple: A tuple of booleans indicating the presence of different character types.
Authors:
    Aquilas DJENONTIN
"""


def string_validators(s):
    """
    Docstring for string_validators
    :param s: The input string to validate.
    :return: A tuple of booleans indicating the presence of different character types.
    This function checks if the string contains at least one alphanumeric character,
    at least one alphabetic character, at least one digit, at least one lowercase letter,
    and at least one uppercase letter.
    """
    has_alnum = any(c.isalnum() for c in s)
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)

    return has_alnum, has_alpha, has_digit, has_lower, has_upper


# Example usage
if __name__ == "__main__":
    s = input()
    alnum, alpha, digi, low, upp = string_validators(s)
    print(alnum)
    print(alpha)
    print(digi)
    print(low)
    print(upp)
