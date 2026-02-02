# MergeTheTools.py
"""
This module contains two implementations of the function `merge_the_tools`
that splits a string into substrings of length k and removes duplicate characters
from each substring.
Each implementation uses a different approach to achieve the same result.
Author: Aquilas DJENONTIN
"""


def merge_the_tools(string, k):
    """
    Function to split the string into substrings of length k and remove duplicates.
    :param string: The input string to be processed.
    :param k: The length of each substring.
    using set to track seen characters for uniqueness.
    1. Iterate over the string in steps of k to create substrings.
    2. For each substring, use a set to track characters that have already been added.
    3. Build a new substring with unique characters and print it.
    """
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print("".join(result))


def merge_the_tools1(string, k):
    # Alternative implementation without using set
    """
    Docstring for merge_the_tools1
    :param string: Description
    :param k: Description
    Function to split the string into substrings of length k and remove duplicates without using set.
    1. Create substrings of length k.
    2. For each substring, iterate through characters and build a new substring by checking if
    they have already been added.
    3. Print the new substring with unique characters.
    """
    substrings = [string[i : i + k] for i in range(0, len(string), k)]
    for wd in substrings:
        newWd = ""
        for ch in wd:
            if ch not in newWd:
                newWd += ch
        print(newWd)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
