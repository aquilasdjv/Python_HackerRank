# SwapCase.py
"""
Docstring for SwapCase
You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
Input Format
The first line contains a single string S.
Output Format
Print the modified string S.
Example:
Input:
HackerRank.com presents "Pythonist 2".
Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
Authored by: Aquilas DJENONTIN
"""


def swap_case(s):
    """
    Docstring for swap_case
    :param s: Description
    :return: Description
    use the built-in method swapcase() to solve the challenge
    """
    return s.swapcase()


def swap_case1(s):
    """
    Docstring for swap_case1
    :param s: Description
    :return: Description
    without using the built-in method swapcase() to solve the challenge
    """
    temp = ""
    for ch in s:
        if ch.isupper():
            temp += ch.lower()
        else:
            temp += ch.upper()
    return temp


if __name__ == "__main__":
    s = input()
    print(swap_case(s))
