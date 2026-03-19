# TheMinionGame.py
"""
This module implements the Minion Game, where two players, Kevin and Stuart,
compete to form substrings from a given string.
Authors: Aquilas DJENONTIN
"""


def minion_game(string):
    """
    Docstring for minion_game
    :param string: Description
    The input string from which substrings are formed.
    :return: Description
    This function calculates and prints the scores of Kevin and Stuart based on the substrings they can
    form from the input string.
    """
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    string_length = len(string)

    for i in range(string_length):
        if string[i] in vowels:
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


def minion_game1(string):
    """
    Docstring for minion_game1
    :param string: Description
    The input string from which substrings are formed.
    :return: Description
    This function calculates and prints the scores of Kevin and Stuart based on the substrings they can
    form from the input string.
    """
    n = len(string)
    vowels = {"A", "E", "I", "O", "U"}
    kevinWord = sum(n - i for i, ch in enumerate(string) if ch in vowels)
    totalScore = n * (n + 1) // 2
    stuartWord = totalScore - kevinWord
    if kevinWord > stuartWord:
        print(f"Kevin {kevinWord}")
    elif kevinWord < stuartWord:
        print(f"Stuart {stuartWord}")
    else:
        print("Draw")


# Example usage
if __name__ == "__main__":
    s = input("Enter the string: ").upper()
    minion_game(s)
