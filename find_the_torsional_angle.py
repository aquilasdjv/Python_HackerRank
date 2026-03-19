# Find the Torsional Angle
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
"""
Docstring for FindtheTorsionalAngle
You are given four points A, B, C and D in a 3D Cartesian coordinate system. You have to find the angle between the plane formed by points A, B and C and the plane formed by points B, C and D. The angle should be in degrees.
Input Format
The first line contains the coordinates of point A separated by a space.
The second line contains the coordinates of point B separated by a space.
The third line contains the coordinates of point C separated by a space.
The fourth line contains the coordinates of point D separated by a space.
Constraints
-100 <= x, y, z <= 100
Output Format
Print the angle between the two planes in degrees, correct up to 2 decimal places.
Sample Input
1 0 0
0 1 0
0 0 0
0 0 1
Sample Output
90.00
Explanation
The plane formed by points A, B and C is the XY plane and the plane formed by points B, C and D is the YZ plane. The angle between these two planes is 90 degrees.
Author: Aquilas DJENONTIN
"""

import math


class Points(object):
    """A class to represent points in a 3D Cartesian coordinate system and perform basic operations on them."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        """Subtract two points to get a vector.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        """Calculate the dot product of two vectors.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        """Calculate the cross product of two vectors.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x,
        )

    def absolute(self):
        """Calculate the magnitude of a vector.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)


# The main function to read input, calculate the angle and print the result.
if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
