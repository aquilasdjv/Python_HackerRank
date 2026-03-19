# HTML Parser Part 1 and Part 2
# https://www.hackerrank.com/challenges/html-parser-part-1/problem
# https://www.hackerrank.com/challenges/html-parser-part-2/problem
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
"""
Docstring for HtmlParser
This module contains a class MyHTMLParser that inherits from HTMLParser and overrides its methods to handle
different parts of the HTML content, such as start tags, end tags, empty tags, data and comments.
Author: Aquilas DJENONTIN
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """
    A class to parse HTML content and extract information about tags, attributes, data and comments.
    This class inherits from HTMLParser and overrides its methods to handle different parts of the HTML content.
    """

    # Part 1: Handle start tags, end tags, and empty tags
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    # Part 2: Handle start tags, end tags, and data
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)


if __name__ == "__main__":
    n = int(input())
    parser = MyHTMLParser()
    s = ""
    for _ in range(n):
        s += input() + "\n"
    parser.feed(s)
