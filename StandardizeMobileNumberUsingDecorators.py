# Standardize Mobile Number Using Decorators
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""
Docstring for StandardizeMobileNumberUsingDecorators
You are given a list of mobile phone numbers. Your task is to write a decorator function that
standardizes the mobile phone numbers in the list. The standardized format should be +91 xxxxx xxxxx, where x is a digit.
Input Format
The first line contains an integer N, the number of mobile phone numbers in the list.
The next N lines contain the mobile phone numbers.
Constraints
1 <= N <= 100
Each mobile phone number contains only digits and may have a country code (e.g., 91
) at the beginning.
Output Format
Output the standardized mobile phone numbers in sorted order, each on a new line.
Sample Input
3
07895462130
919875641230
9195969878
Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
Explanation
The input mobile phone numbers are standardized to the format +91 xxxxx xxxxx. The standardized numbers are then sorted and printed in the required format.
Author: Aquilas DJENONTIN
"""


def wrapper(f):
    """
    A decorator function to standardize mobile numbers in a list.
    Complexity: O(n log n) due to the sorting step, where n is the number of phone numbers in the list.
    """

    def fun(l):
        def format_number(x):
            s = str(int(x))
            n = len(s)
            if n == 10:
                return f"+91 {s[:5]} {s[5:]}"
            else:
                return f"+{s[:2]} {s[2:7]} {s[7:]}"

        a = [format_number(x) for x in l]
        a.sort()
        print(*a, sep="\n")
        return a

    return fun


def wrapper_v2(f):
    """
    A decorator function to standardize mobile numbers in a list using list comprehension.
    Complexity: O(n log n) due to the sorting step, where n is the number of phone numbers in the list.
    """

    def fun(l):
        a = [f"+91 {x[-10:-5]} {x[-5:]}" for x in l]
        a.sort()
        print(*a, sep="\n")
        return a

    return fun


def wrapper_v3(f):
    """
    A decorator function to standardize mobile numbers in a list using a more detailed approach.
    Complexity: O(n log n) due to the sorting step, where n is the number of phone numbers in the list.
    """

    def fun(l):
        a = []
        for x in l:
            if len(str(int(x))) == 10:
                a.append(("+91", str(int(x))[:5], str(int(x))[5:]))
            else:
                a.append((f"+{str(int(x))[:2]}", str(int(x))[2:7], str(int(x))[7:]))
        a.sort(key=lambda x: (x[0], x[1], x[2]))
        b = [" ".join(x) for x in a]
        print(*b, sep="\n")
        return list(b)

    return fun


@wrapper
def sort_phone(l):
    """A function to sort and standardize phone numbers using the wrapper decorator."""
    print(*sorted(l), sep="\n")


# Example usage:
if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
