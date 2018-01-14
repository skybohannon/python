# 26. Write a Python program to display formatted text (width=50) as output.

import textwrap

text_block = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. " \
             "Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts " \
             "in fewer lines of code than possible in languages such as C++ or Java."

print(textwrap.fill(text_block, width=50))