def python_food():
    text = "Spam and eggs"


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    return " " * left_margin + text

# with open ("centered", mode='w') as centered_file:
# s1 = center_text("spam and eggs")
# print(s1)
# s2 = center_text(12)
# print(s2)
# s3 = center_text("spam spam spam spam")
# print(s3)
# s4 = center_text("first", "second", 3, 4, "spam", sep=':')
# print(s4)

with open("menu", 'w') as menu:
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text(12)
    print(s2, file=menu)
    print(center_text(12), file=menu)
    s4 = center_text("first", "second", 3, 4, "spam", sep=':')
    print(s4, file=menu)