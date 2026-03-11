# Decorators 2 - Name Directory
# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
"""
Docstring for DecoratorsNameDirectory
You are given a list of people with their first name, last
 name, age, and sex. Your task is to write a decorator function that sorts the list of people by
 their age and formats their names with appropriate titles (Mr. for males and Ms. for females).
Input Format
The first line contains an integer N, the number of people in the list.
The next N lines contain the first name, last name, age, and sex of each person, separated by spaces.
Constraints
1 <= N <= 100
Each person's age is a positive integer
Output Format
Output the sorted and formatted list of people, each on a new line.
Sample Input
3
John Doe 25 M
Jane Smith 30 F
Alice Johnson 22 F
Sample Output
Ms. Alice Johnson
Mr. John Doe
Ms. Jane Smith
Explanation
The input list of people is sorted by age in ascending order. The names are formatted with appropriate titles based on their sex.
The sorted and formatted list is then printed in the required format.
Author: Aquilas DJENONTIN
"""

import operator


def person_lister(f):
    """
    A decorator function to sort a list of people by their age and format their names with appropriate titles.
    Complexity: O(n log n) due to the sorting step, where n is the number of people in the list.
    """

    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return [
            ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
            for person in people
        ]

    return inner


def person_lister_v2(f):
    """
    A decorator function to sort a list of people by their age and format their names with appropriate titles using sorted() and operator.itemgetter.
    Complexity: O(n log n) due to the sorting step, where n is the number of people in the list.
    """

    def inner(people):
        people = sorted(people, key=lambda p: int(operator.itemgetter(2)(p)))
        return [
            ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
            for person in people
        ]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")
