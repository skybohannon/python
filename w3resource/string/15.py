# 15. Write a Python function to create the HTML string with tags around the word(s). Go to the editor
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


def add_tags(a, b):
    return "<"+a+">" + b + "</"+a+">"

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
