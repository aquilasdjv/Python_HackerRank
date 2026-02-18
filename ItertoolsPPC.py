# Iteertools Product Permutation Combination Combinations_with_replacement
# https://docs.python.org/3/library/itertools.html

from itertools import product, permutations, combinations, combinations_with_replacement

"""
Docstring for ItertoolsPPC
This module demonstrates the use of various functions from the itertools library in Python, including product, permutations
, combinations, and combinations_with_replacement. Each function is showcased through a dedicated demo function that illustrates its functionality with example inputs and outputs.
The product_demo function demonstrates how to compute the Cartesian product of two lists of integers, generating all
possible pairs of elements. The permutations_demo function illustrates how to generate all possible permutations of a given string for a specified length. 
The combinations_demo function shows how to generate all possible combinations of characters from a string for a specified length, without repetition. 
Finally, the combinations_with_replacement_demo function demonstrates how to generate combinations of characters from a string for a specified length, allowing for repeated characters.
Each demo function reads input from the user, processes it using the respective itertools function, and prints
the results in a clear and organized manner. The module is designed to provide a comprehensive overview of these itertools functions, making it easier for users to understand and utilize them in their own projects.
Constraints:
- The input for the product_demo function should consist of two lines, each containing space-separated integers.
- The input for the permutations_demo, combinations_demo, and combinations_with_replacement_demo functions should
consist of a single line, where the first part is a string and the second part is an integer n.
- The integer n should be less than or equal to the length of the input string for the
permutations_demo and combinations_demo functions to avoid generating permutations or combinations of length greater than the number of available characters.
- The integer n can be any positive integer for the combinations_with_replacement_demo function, as combinations with replacement allow for repeated characters.
Complexity:
- The time complexity for the product_demo function is O(m*n), where m and n are the lengths of the two input lists, since we need to generate all possible pairs.
- The time complexity for the permutations_demo function is O(k!/(k-n)!), where
k is the length of the input string and n is the length of the permutations, since we need to generate all possible permutations of length n from k characters.
- The time complexity for the combinations_demo function is O(k!/(n!(k-n)!
), where k is the length of the input string and n is the length of the combinations, since we need to generate all possible combinations of length n from k characters.
- The time complexity for the combinations_with_replacement_demo function is O(k!/(n!(k-n)!)), 
where k is the length of the input string and n is the length of the combinations, since we need to generate all possible combinations of length n from k characters with replacement.
Author: Aquilas DJENONTIN
"""


# Product
def product_demo():
    """
    Docstring for product_demo
    This function demonstrates the use of the itertools.product function, which computes the Cartesian product of input iterables.
    It takes two lists of integers as input and generates all possible pairs of elements,
    where the first element is from the first list and the second element is from the second list.
    The output is a list of tuples representing these pairs.
    For example, if the input lists are A = [1, 2] and B = [3, 4], the output will be:
    [(1, 3), (1, 4), (2, 3), (2, 4)]
    The function reads two lines of input, where each line contains space-separated integers.
    It then uses the product function to compute the Cartesian product of the two lists and prints the result as a list of tuples.
    Constraints:
    - The input lists can contain any number of integers, but for demonstration purposes,
    we can assume they will contain a reasonable number of elements (e.g., up to 10).
    Complexity: O(m*n) for time complexity, where m and n are the lengths of the two input lists, since we need to generate all possible pairs.
    """
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    prod = product(A, B)
    print(list(prod))  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]


# Permutations
def permutations_demo():
    """
    Docstring for permutations_demo
    This function demonstrates the use of the itertools.permutations function, which generates all possible permutations of a given iterable.
    It takes a string and an integer n as input, where the string represents a set of characters and n represents the length of the permutations to be generated.
    The function generates all possible permutations of the characters in the string of length n and prints them in sorted order.
    For example, if the input string is "HAC" and n is 2, the output will be:
    [('H', 'A'), ('H', 'C'), ('A', 'H'), ('A', 'C'), ('C', 'H'), ('C', 'A')]
    The function reads a single line of input, where the first part is the string and the second part is the integer n.
    It then uses the permutations function to generate the desired permutations and prints them as a list of tuples.
    Constraints:
    - The input string can contain any number of characters, but for demonstration purposes, we can assume it will contain a reasonable number of characters (e.g., up to 10).
    - The integer n should be less than or equal to the length of the input string to avoid generating permutations of length greater than the number of available characters.
    Complexity: O(k!/(k-n)!) for time complexity, where k is the length of the input string and n is the length of the permutations,
    since we need to generate all possible permutations of length n from k characters.
    """
    s, n = input().split()
    for x in sorted(["".join(list(y)) for y in permutations(s, int(n))]):
        print(
            x
        )  # Output: [('H', 'A', 'C'), ('H', 'C', 'A'), ('A', 'H', 'C'), ('A', 'C', 'H'), ('C', 'H', 'A'), ('C', 'A', 'H')]


# Combinations
def combinations_demo():
    """
    Docstring for combinations_demo
    This function demonstrates the use of the itertools.combinations function, which generates all possible combinations of a given iterable.
    It takes a string and an integer n as input, where the string represents a set of characters and n represents the length of the combinations to be generated.
    The function generates all possible combinations of the characters in the string of length n and prints them in sorted order.
    For example, if the input string is "HAC" and n is 2, the output will be:
    [('H', 'A'), ('H', 'C'), ('A', 'C')]
    The function reads a single line of input, where the first part is the string and the second part is the integer n.
    It then uses the combinations function to generate the desired combinations and prints them as a list of tuples.
    Constraints:
    - The input string can contain any number of characters, but for demonstration purposes, we can
    assume it will contain a reasonable number of characters (e.g., up to 10).
    - The integer n should be less than or equal to the length of the input string to
    avoid generating combinations of length greater than the number of available characters.
    Complexity: O(k!/(n!(k-n)!)) for time complexity, where k
    is the length of the input string and n is the length of the combinations, since we need to generate all possible combinations of length n from k characters.
    """
    s, n = input().split()
    for x in sorted(["".join(list(y)) for y in combinations(s, int(n))]):
        print(x)  # Output: [('H', 'A'), ('H', 'C'), ('A', 'C')]


# Combinations with replacement
def combinations_with_replacement_demo():
    """
    Docstring for combinations_with_replacement_demo
    This function demonstrates the use of the itertools.combinations_with_replacement function, which generates all possible combinations of a given iterable with replacement.
    It takes a string and an integer n as input, where the string represents a set of characters and n represents the length of the combinations to be generated.
    The function generates all possible combinations of the characters in the string of length n, allowing for repeated characters, and prints them in sorted order.
    For example, if the input string is "HAC" and n is 2, the output will be:
    [('H', 'H'), ('H', 'A'), ('H', 'C'), ('A', 'A'), ('A', 'C'), ('C', 'C')]
    The function reads a single line of input, where the first part is the string and the second part is the integer n.
    It then uses the combinations_with_replacement function to generate the desired combinations and prints them as a list of tuples.
    Constraints:
    - The input string can contain any number of characters, but for demonstration purposes, we can assume it will contain a reasonable number of characters (e.g., up to 10).
    - The integer n can be any positive integer, as combinations with replacement allow for repeated characters.
    Complexity: O(k!/(n!(k-n)!)) for time complexity, where k is the length of the input string and n is the length of the combinations,
    since we need to generate all possible combinations of length n from k characters with replacement.
    """
    s, n = input().split()
    for x in sorted(
        ["".join(list(y)) for y in combinations_with_replacement(s, int(n))]
    ):
        print(
            x
        )  # Output: [('H', 'H'), ('H', 'A'), ('H', 'C'), ('A', 'A'), ('A', 'C'), ('C', 'C')]


# Example usage:
if __name__ == "__main__":
    # product_demo()
    # permutations_demo()
    # combinations_demo()
    combinations_with_replacement_demo()
