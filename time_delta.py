# Time Delta
# https://www.hackerrank.com/challenges/python-time-delta/problem
"""
Docstring for TimeDelta
Given two timestamps, find the absolute difference (in seconds) between them.
Input Format
The first line contains T, the number of test cases. Each test case contains 2 lines, each representing a timestamp in the format: Day dd Mon yyyy hh:mm:ss +xxxx
Constraints
1 <= T <= 10
The year is between 2000 and 3000.
Output Format
Output the absolute difference (in seconds) between the two timestamps.
Sample Input
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output
25200
88200
Explanation
In the first test case, the difference is 7 hours, which is 25200 seconds. In the second test case, the difference is 24 hours and 30 minutes, which is 88200 seconds.
Author: Aquilas DJENONTIN
"""

import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    """
    Given two timestamps, find the absolute difference (in seconds) between them.
    Complexity: O(1) since we are using built-in functions that run in constant time.
    """
    year1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    year2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return f"{int((year1 - year2).total_seconds()).__abs__()}"


# Example usage:
if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + "\n")

    fptr.close()
