# Polar Coordinates
# https://www.hackerrank.com/challenges/polar-coordinates
"""
Docstring for PolarCoordinates
This module contains two functions, polar_coordinates and polar_coordinates_v2, which convert a complex number from Cartesian to Polar coordinates.
The first function uses regular expressions to extract the real and imaginary parts of the complex number,
while the second function uses the built-in complex function to directly convert the string representation of the complex number into a complex number.
Both functions then calculate the magnitude and phase using the cmath module and return the phase (angle) of the complex number in radians.
As the input is a string representation of a complex number, the functions will handle the conversion and return the desired output.
Author: Aquilas DJENONTIN
"""

import re
import cmath


def polar_coordinates(s):
    """
    Convert a complex number from Cartesian to Polar coordinates.
    Args:
        s (str): A string representation of a complex number in Cartesian coordinates (e.g., '1+2j').
    Returns:
        float: The phase (angle) of the complex number in radians.
    using regular expressions to extract the real and imaginary parts of the complex number, then calculating the magnitude and phase using the cmath module.
    """
    pattern = r"([+-]?\d*\.?\d+)([+-]\d*\.?\d+)j"
    matche = re.match(pattern, s)

    if matche:
        x = float(matche.group(1))
        y = float(matche.group(2))
        print((x**2 + y**2) ** 0.5)
        return cmath.phase(complex(x, y))


def polar_coordinates_v2(s):
    """
    Convert a complex number from Cartesian to Polar coordinates using the built-in complex function.
    Args:
        s (str): A string representation of a complex number in Cartesian coordinates (e.g., '1+2j').
    Returns:
        float: The phase (angle) of the complex number in radians.
    This function uses the built-in complex function to convert the string representation of the complex number directly
    into a complex number, then calculates the magnitude and phase using the cmath module.
    """
    z = complex(s)
    print(abs(z))
    return cmath.phase(z)


if __name__ == "__main__":
    z = input()
    print(polar_coordinates(z))
