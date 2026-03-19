# Default Arguments
# https://www.hackerrank.com/challenges/default-arguments/problem
"""
Docstring for DefaultArguments
You are given a function with default arguments. Your task is to find the value of the default argument and print it.
Input Format
The first line contains an integer T, the number of test cases.
The next T lines contain a string S, the name of the function.
Constraints
1 <= T <= 100
Output Format
For each test case, print the value of the default argument for the given function.
Sample Input
3
print_from_stream
print_from_stream odd
print_from_stream even
Sample Output
0
1
2
Explanation
The default argument for the print_from_stream function is 0, which is the starting point for the EvenStream. When we call print_from_stream with the argument 'odd', it uses the OddStream, which starts at 1. When we call print_from_stream with the argument 'even', it uses the EvenStream, which starts at 0.
Author: Aquilas DJENONTIN
"""


class OddStream:
    """A class to generate an infinite stream of odd numbers."""

    def __init__(self):
        self.current = 1

    def get_next(self):
        """
        Return the next odd number in the stream.
        Complexity: O(1) since we are performing a constant number of operations.
        """
        num = self.current
        self.current += 2
        return num


class EvenStream(OddStream):
    """A class to generate an infinite stream of even numbers."""

    def __init__(self):
        self.current = 0


def print_from_stream(n, stream=None):
    """
    Print the first n numbers from the given stream. If no stream is provided, use the EvenStream by default.
    Complexity: O(n) since we are printing n numbers from the stream.
    """
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


# Example usage:
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        stream_name, n = map(str, input().split())
        if stream_name == "odd":
            print_from_stream(int(n), OddStream())
        elif stream_name:
            print_from_stream(int(n))
