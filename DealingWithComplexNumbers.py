# Dealing with Complex Numbers
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""
Docstring for DealingWithComplexNumbers
You are given two complex numbers, and you have to perform the following operations on them:
Addition, Subtraction, Multiplication, Division, and Modulus.
Input Format
The first line contains the real and imaginary part of the first complex number separated by a space.
The second line contains the real and imaginary part of the second complex number separated by a space.
Constraints
-100 <= real, imaginary <= 100
Output Format
For each operation, print the result on a separate line. The output should be in the form
a+bi where a is the real part and b is the imaginary part. The modulus should be printed as a+0.00i.
Sample Input
2 1
5 6
Sample Output
7.00+7.00i
-3.00-5.00i
-4.00+16.00i
0.00+6.32i
2.24+0.00i
Explanation
Let the first complex number be A = 2 + i and the second complex number be B
= 5 + 6i. Then:
A + B = 7 + 7i
A - B = -3 - 5i
A * B = -4 + 16i
A / B = 0.00 + 6.32i
|A| = 2.24 + 0.00i
Author: Aquilas DJENONTIN
"""
import math


class Complex(object):
    """A class to represent complex numbers and perform basic operations on them."""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        """
        Add two complex numbers.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        """
        Subtract two complex numbers.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        """
        Multiply two complex numbers.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Complex(
            (self.real * no.real) - (self.imaginary * no.imaginary),
            (self.real * no.imaginary) + (self.imaginary * no.real),
        )

    def __truediv__(self, no):
        """
        Divide two complex numbers.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        d = no.real**2 + no.imaginary**2
        return Complex(
            ((self.real * no.real) + (self.imaginary * no.imaginary)) / d,
            ((self.imaginary * no.real) - (self.real * no.imaginary)) / d,
        )

    def mod(self):
        """
        Calculate the modulus of a complex number.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        """
        Return the string representation of the complex number in the form a+bi.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


# Example usage:
if __name__ == "__main__":
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep="\n")
