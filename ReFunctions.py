# Regular Expressions in Python
# https://www.hackerrank.com/challenges/re-start-re-end/problem
# https://www.hackerrank.com/challenges/re-group-groups/problem
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# https://www.hackerrank.com/challenges/re-split/problem
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
"""
Docstring for ReFunctions
This module contains functions that demonstrate the use of regular expressions in Python.
Author: Aquilas DJENONTIN
"""
import re


def split_number():
    """
    A function to split a number by commas and dots using regular expressions.
    Complexity: O(n) since we are iterating through the input string once.
    """
    # This pattern matches commas and dots in the input string.
    regex_pattern = r"[,.]"
    print("\n".join(re.split(regex_pattern, input())))


def group_demo():
    """
    A function to demonstrate the use of groups in regular expressions.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches any character that is followed by the same character one or more times, using a backreference to the first group.
    regex_pattern = r"([a-zA-Z0-9])\1+"
    match = re.search(regex_pattern, input())
    if match:
        print(match.group(1))
    else:
        print(-1)


def findall_demo():
    """
    A function to demonstrate the use of findall in regular expressions.
    Complexity: O(n) since we are iterating through the input string once.
    """
    # This pattern matches sequences of two or more vowels that are surrounded by consonants, ignoring case.
    regex_pattern = (
        r"(?i)(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])"
    )
    matches = re.findall(regex_pattern, input())
    if matches:
        print(*matches, sep="\n")
    else:
        print(-1)


def start_end_demo():
    """
    A function to demonstrate the use of start and end in regular expressions.
    Complexity: O(n) since we are iterating through the input string once.
    """
    s = input()
    k = input()
    # This pattern uses a positive lookahead to find all occurrences of the substring k in the string s, including overlapping matches.
    pattern = re.compile(r"(?={})".format(re.escape(k)))
    matches = list(pattern.finditer(s))

    if not matches:
        print((-1, -1))
    else:
        for m in matches:
            print((m.start(), m.start() + len(k) - 1))


def sub_demo():
    """
    A function to replace '&&' with 'and' and '||' with 'or' in a given string using regular expressions.
    Complexity: O(n) since we are iterating through the input string once for each substitution.
    """
    pattern_and = r"(?<=\s)[&]{2}(?=\s)"
    pattern_or = r"(?<=\s)[|]{2}(?=\s)"

    n = int(input())
    for _ in range(n):
        a = input()
        b = re.sub(pattern_and, "and", a)
        c = re.sub(pattern_or, "or", b)
        print(c)


# The main function to call the split_number and group_demo functions.
if __name__ == "__main__":
    split_number()
    group_demo()
    findall_demo()
    start_end_demo()
    sub_demo()
