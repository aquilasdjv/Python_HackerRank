# Nested_Lists.py
"""
Docstring for Nested_Lists
This module finds the names of students with the second lowest grade
from a list of student names and their grades.
Example:
Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Output:
Berry
Harry
Instructions:
1. Read an integer n from input, the number of students.
2. Read n pairs of lines, each containing a student's name and grade.
3. Determine the second lowest grade and print the names of all students
   who have that grade, in alphabetical order.
Author: aquilas DJENONTIN
"""

if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = sorted({score for name, score in records})
    second_lowest_score = scores[1]
    names_with_second_lowest = sorted(
        [name for name, score in records if score == second_lowest_score]
    )
    for name in names_with_second_lowest:
        print(name)
