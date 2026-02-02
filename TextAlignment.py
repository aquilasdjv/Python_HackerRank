# TextAlignment.py
"""
Docstring for TextAlignment
This script prints a pattern of text aligned in a specific format based on the input thickness.
The pattern consists of a top cone, top pillars, a middle belt, bottom pillars, and
a bottom cone.
The thickness of the pattern is determined by an odd integer input.
Author: Aquilas DJENONTIN
"""

# Read odd thickness
thickness = int(input().strip())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness - i - 1)).rjust(thickness) + c + (c*(thickness - i - 1)).ljust(thickness)).rjust(thickness*6))