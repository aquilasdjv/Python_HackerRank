# Finding_The_Percentage.py
"""
Docstring for Finding_The_Percentage
This script calculates the average score of a student based on their scores provided in the input.
Each student's name is associated with a list of their scores.
Example usage:
Input:
3
John 85 90 80
Jane 90 95 100
Doe 70 75 80
Output:
95.00
Author: Aquilas DJENONTIN
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average_score:.2f}")
