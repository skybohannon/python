# 29. Write a Python program to set the indentation of the first line.

import textwrap

text_block = '''Python is a widely used high-level, general-purpose, interpreted, dynamic 
            programming language. Its design philosophy emphasizes code readability, and 
            its syntax allows programmers to express concepts in fewer lines of code than 
            possible in languages such as C++ or Java.'''

text_dedent = textwrap.dedent(text_block).strip()
print(textwrap.fill(text_dedent, initial_indent="", subsequent_indent=" " * 4, width=80))