# Write_a_function.py

"""
Docstring for Write_a_function
This function checks if a given year is a leap year.
A year is a leap year if it is divisible by 4, except for end-of-century years,
which must be divisible by 400.
# For example, 2000 is a leap year, but 1900 is not.
# The function returns True if the year is a leap year, otherwise it returns False.
# Example usage:
# print(is_leap(2020))  # Output: True
# print(is_leap(1900))  # Output: False
@author aquilas djenontin
"""


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))
