# FindaString.py
"""
Docstring for FindaString
This module contains functions to count occurrences of a substring within a string.
Function: count_substring, count_substring1
Parameters:
    string (str): The main string in which to search for the substring.
    substring (str): The substring to count within the main string.
Returns:
    int: The number of occurrences of the substring in the main string.
Authors:
    Aquilas DJENONTIN
"""


def count_substring(string, substring):
    """
    Docstring for count_substring
    :param string: The main string in which to search for the substring.
    :param substring: The substring to count within the main string.
    :return: The number of occurrences of the substring in the main string.
    This function counts how many times a given substring appears in a string.
    """
    count = 0
    substring_length = len(substring)
    for i in range(len(string) - substring_length + 1):
        if string[i : i + substring_length] == substring:
            count += 1
    return count


def count_substring1(string, sub_string):
    """
    Docstring for count_substring1
    :param string: The main string in which to search for the substring.
    :param sub_string: The substring to count within the main string.
    :return: The number of occurrences of the substring in the main string.
    This function counts how many times a given substring appears in a string using a different approach.
    """
    countSub = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            countSub += 1
    return countSub


# Example usage
if __name__ == "__main__":
    main_string = input("Enter the main string: ")
    sub_string = input("Enter the substring to count: ")
    result = count_substring(main_string, sub_string)
    print(f"The substring '{sub_string}' occurs {result} times in the main string.")
