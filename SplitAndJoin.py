# SplitAndJoin.py
"""
Docstring for SplitAndJoin
This module contains a function to split a string into words and then join them with hyphens.
Function: split_and_join
Parameters:
    line (str): The input string to be processed.
Returns:
    str: The processed string with words joined by hyphens.
Authors:
    Aquilas DJENONTIN
"""


def split_and_join(line):
    """
    Docstring for split_and_join
    :param line: The input string to be processed.
    :return: The processed string with words joined by hyphens.
    This function splits a string into words and joins them with hyphens.
    """
    # Split the line into words
    words = line.split(" ")
    # Join the words with hyphens
    joined_line = "-".join(words)
    return joined_line


def split_and_join1(line):
    """
    Docstring for split_and_join1
    :param line: Description
    :return: Description
    This function splits a string into words and joins them with hyphens.
    """
    # One-liner implementation of split and join
    return "-".join(line.split(" "))


# Example usage
if __name__ == "__main__":
    input_line = input("Enter a line of text: ")
    result = split_and_join(input_line)
    print(result)  # Output: This-is-a-sample-line
