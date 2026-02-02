"""
This module provides functionality to wrap text to a specified width.
It includes a function `wrap_text` that utilizes the `textwrap` library
to format text.
And a custom `wrap` function that manually wraps a string into lines of a given width.
Example usage:
    wrapped = wrap_text("This is an example string that needs to be wrapped.", 10)
    print(wrapped)
The output will be:
This is an
example
string
that needs
to be
wrapped.
Author: Aquilas DJENONTIN
"""
# TextWraps.py
import textwrap as tw


def wrap_text(text, width):
    """
    Wraps the input text to the specified width.
    Parameters:
    text (str): The text to be wrapped.
    width (int): The maximum width of each line.
    Returns:
    str: The wrapped text.
    """
    return tw.fill(text, width)


def wrap(string, max_width):
    """
    A function that wraps a string into a paragraph of a specified width.
    Parameters:
    string (str): The string to be wrapped.
    max_width (int): The maximum width of each line.
    Returns:
    str: The wrapped string.
    """
    out = ""
    for i in range(0, len(string), max_width):
        out += (
            string[i : i + max_width] + "\n"
            if (i + max_width) < len(string)
            else string[i:]
        )
    return out


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
