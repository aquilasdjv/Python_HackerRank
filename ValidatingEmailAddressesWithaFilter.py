# Validating Email Addresses With a Filter
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""
Docstring for ValidatingEmailAddressesWithaFilter
You are given a list of n email addresses. Your task is to filter out the valid email addresses and print them in lexicographical order.
Input Format
The first line contains an integer n, the number of email addresses.
The next n lines each contain an email address.
Constraints
Each line is a non-empty string.
Output Format
Print the valid email addresses in lexicographical order, one per line.
Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
Explanation
All three email addresses are valid, so we print them in lexicographical order.
Author: Aquilas DJENONTIN
"""
import re


def fun(s):
    # return True if s is a valid email, else return False
    """
    A function to validate an email address using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    email_parten = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$"
    return bool(re.fullmatch(email_parten, s))


def filter_mail(emails):
    """
    A function to filter out valid email addresses from a list of email addresses.
    Complexity: O(n) since we are iterating through the list of email addresses once.
    """
    return list(filter(fun, emails))


# The main function to read input, filter valid email addresses and print the result.
if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
