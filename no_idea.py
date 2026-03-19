# No Idea
"""
Docstring for NoIdea
This module contains a function to calculate a score based on the presence of elements from a list in
two sets. The function reads input from the user, processes it, and prints the result. The code includes a test case to demonstrate the functionality of the noIdea function.
Authors: Aquilas DJENONTIN
"""


def noIdea():
    """
    Docstring for noIdea function
    This function reads input from the user, processes it, and prints the result. It takes
    three lines of input: the first line contains two integers n and m, the second line contains a list of integers, and the third and fourth lines contain sets of integers.
    The function calculates a score based on the presence of elements from the list in the two sets and prints the final score.
    Parameters:
    None: This function does not take any parameters. It reads input directly from the user.
    Returns:
    None: This function does not return any value. It prints the result directly to the console.
    Complexity: O(n) where n is the number of elements in the input list, due to the iteration to calculate the score based on the presence of elements in the sets.
    """
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    h = 0
    for i in l:
        if i in a:
            h += 1
        elif i in b:
            h -= 1

    print(h)


if __name__ == "__main__":
    noIdea()
