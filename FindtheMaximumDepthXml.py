# XML2 - Find the Maximum Depth
# https://www.hackerrank.com/challenges/xml-2-find-the-maximum-depth/problem
"""
Docstring for FindtheMaximumDepthXml
You are given an XML document, and you have to find the maximum depth of the document.
The depth of an XML document is the maximum number of nested elements in the document.
Input Format
The first line contains the number of lines in the XML document. The subsequent lines contain the XML document.
Constraints
1 <= Number of lines in XML document <= 100
Output Format
Output a single line containing the maximum depth of the XML document.
Sample Input
5
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='en' href='http://www.hackerrank.com'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output
2
Explanation
The XML document has a maximum depth of 2. The feed element is at depth 1, and the title,
subtitle, link, and updated elements are at depth 2. Hence, the maximum depth of the XML document is 2.
Author: Aquilas DJENONTIN
"""
import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    """
    Recursively calculate the maximum depth of the XML tree.
    Complexity: O(n) where n is the total number of nodes in the XML tree, since we visit each node once.
    """
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)

# Example usage:
if __name__ == "__main__":
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
