# Find the Score XML
# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
"""
Docstring for FindtheScoreXml
You are given an XML document, and you have to find the score of the document.
The score of an XML document is the sum of the number of attributes in each element in the document.
Input Format
The first line contains the number of lines in the XML document. The subsequent lines contain the XML document.
Constraints
1 <= Number of lines in XML document <= 100
Output Format
Output a single line containing the score of the XML document.
Sample Input
5
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='en' href='http://www.hackerrank.com'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output
5
Explanation
The XML document contains 5 attributes: xml:lang in the feed element, lang in the
subtitle element, and rel, href in the link element. Hence, the score of the XML document is 5.
Author: Aquilas DJENONTIN
"""

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    """
    Recursively count the number of attributes in the XML tree.
    Complexity: O(n) where n is the total number of nodes in the XML tree, since we visit each node once.
    """
    n = len(node.attrib)
    for child in node:
        n += get_attr_number(child)
    return n


# Example usage:
if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
