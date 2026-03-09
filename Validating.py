# Validating Roman Numerals / phone numbers / email address / UID / credit card and postal code
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# https://www.hackerrank.com/challenges/validating-uid/problem
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# https://www.hackerrank.com/challenges/validating-postalcode/problem
"""
Docstring for Validating
This module contains functions that demonstrate the use of regular expressions to validate Roman numerals, phone numbers, email addresses, UIDs, credit card numbers and postal codes.
Author: Aquilas DJENONTIN
"""


import re
import email.utils as eu


def validate_roman():
    # return True if s is a valid Roman numeral, else return False
    """
    A function to validate a Roman numeral using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches a valid Roman numeral according to the problem statement.
    # It allows for up to three 'M's, followed by either 'CM', 'CD', 'D'
    # followed by up to three 'C's, 'XC', 'XL', 'L'
    # followed by up to three 'X's, and 'IX', 'IV', 'V' followed by up to three 'I's.
    roman_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    print(str(bool(re.match(roman_pattern, input()))))


def validate_phone_number():
    # return True if s is a valid phone number, else return False
    """
    A function to validate a phone number using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches a valid phone number according to the problem statement.
    # It starts with 7, 8, or 9, followed by exactly 9 digits.
    phone_pattern = r"^[789]\d{9}$"
    print(str(bool(re.match(phone_pattern, input()))))


def validate_email_address():
    """
    A function to validate an email address using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    But we also use the email.utils module to parse the email address, which adds some overhead.
    """
    # This pattern matches a valid email address according to the problem statement.
    # It starts with a letter, followed by any combination of letters, digits, underscores, dots, or hyphens, then an @ symbol, followed by a domain name and a top-level domain.
    email_patten = r"^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    user_input = input()
    name, email = eu.parseaddr(user_input)
    matches = re.match(email_patten, email)
    if matches:
        print(f"{name} <{email}>")


def validate_uid():
    """
    A function to validate a UID using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches a valid UID according to the problem statement.
    # It must be exactly 10 characters long, contain at least 2 uppercase letters, at least 3 digits, and no character should repeat.
    uid_pattern = r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$"
    print("Valid" if bool(re.match(uid_pattern, input())) else "Invalid")


def validate_credit_card():
    """
    A function to validate a credit card number using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches a valid credit card number according to the problem statement.
    # It must start with 4, 5, or 6, followed by exactly 15 digits or 16 digits if it is separated by hyphens.
    # It should not contain any other characters and should not have four or more consecutive repeated digits.
    credit_card_pattern = r"^(?!.*(\d)(?:-?\1){3})([456]\d{3}(-\d{4}){3}|[456]\d{15})$"
    print("Valid" if bool(re.fullmatch(credit_card_pattern, input())) else "Invalid")


def validate_postal_codes():
    """
    A function to validate a postal code using a regular expression.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    # This pattern matches a valid postal code according to the problem statement.
    # It must be a six-digit number in which the first digit is not zero, and it must not contain more than one alternating repetitive digit pair.
    regex_integer_in_range = r"^[1-9]\d{5}$"
    # This pattern matches any digit that is followed by the same digit one or more times,
    # using a positive lookahead to ensure that we are counting pairs of digits that are not separated by other digits.
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
    P = input()
    print(
        bool(re.match(regex_integer_in_range, P))
        and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
    )


# The main function to read input, validate Roman numeral, phone number, email address , UID, credit card and postal code and print the result.
if __name__ == "__main__":
    validate_roman()
    validate_phone_number()
    validate_email_address()
    validate_uid()
    validate_credit_card()
    validate_postal_codes()
