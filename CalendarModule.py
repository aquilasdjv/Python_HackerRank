# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem
"""
Docstring for CalendarModule
Given a date, find what the day is on that date.
Input Format
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
Constraints
2000 < year < 3000
Output Format
Output the correct day in capital letters.
Sample Input
08 05 2015
Sample Output
WEDNESDAY
Explanation
The day on August 5th, 2015 was a Wednesday.
Author: Aquilas DJENONTIN
"""
import calendar


def calendar_demo(month, day, year):
    """
    Given a date, find what the day is on that date.
    Complexity: O(1) since we are using built-in functions that run in constant time.
    """
    weekday_index = calendar.weekday(year, month, day)
    weekday_name = calendar.day_name[weekday_index]
    return weekday_name.upper()
    # return date(year, month, day).strftime("%A").upper()
    # Samething using date from datetime but we use the first due to task requirement


# Example usage:
if __name__ == "__main__":
    month, day, year = map(int, input().split())
    weekday_name = calendar_demo(month, day, year)
    print(weekday_name)
