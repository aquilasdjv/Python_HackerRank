# Find Angle MBC
# https://www.hackerrank.com/challenges/find-angle/problem
"""
Docstring for FindAngleMBC
This program calculates the angle MBC in a right triangle given the lengths of sides AB and BC.
The angle MBC is calculated using the arctangent function, which gives the angle in radians.
M is the center point of the hypotenuse AC, and the angle MBC is the angle formed at point B by the line segments MB and BC.
The result is then converted to degrees and rounded to the nearest whole number before being returned as a string with the degree symbol.
An example usage is provided where the user can input the lengths of AB and BC, and the program will output the angle MBC.
E.g. if AB = 3 and BC = 4, the output will be "The angle MBC is: 37°".
Author: Aquilas DJENONTIN
"""

import math


def find_angle_mbc(ab, bc):
    return f"{round(math.degrees(math.atan(ab/bc)))}\u00b0"


# Example usage:
if __name__ == "__main__":
    ab = int(input("Enter the length of AB: "))
    bc = int(input("Enter the length of BC: "))

    angle_mbc = find_angle_mbc(ab, bc)
    print(f"The angle MBC is: {angle_mbc}")
