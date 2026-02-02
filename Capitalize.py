# Capitalize.py
"""
This module provides functionality to capitalize the first letter of each word in a given string.
It is compatible with both PyPy3 and CPython interpreters.
Authors: Aquilas DJENONTIN
"""


def capitalize_words(input_string):
    """
    Capitalizes the first letter of each word in the input string.
    Parameters:
    input_string (str): The string to be capitalized.
    Returns:
    str: The capitalized string.
    This works on PyPy3 and CPython interpreters.
    """
    return " ".join([word.capitalize() for word in input_string.split()])


def solve(s):
    """
    Docstring for solve
    Capitalizes the first letter of each word in the given string.
    Parameters:
    s (str): The input string to be processed.
    Returns:
    str: The string with each word capitalized.
    s = "example input string for capitalization"
    This works on Python 3.6 and above.
    """
    return " ".join(w[:1].upper() + w[1:] if w else "" for w in s.split(" "))


# Example usage
if __name__ == "__main__":
    test_string = "hello world! this is a test."
    capitalized_string = capitalize_words(test_string)
    print(capitalized_string)  # Output: "Hello World! This Is A Test."
