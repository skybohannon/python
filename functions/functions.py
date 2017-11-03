def python_food():
    text = "Spam and eggs"


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text, end=end, file=file, flush=flush)

center_text("spam and eggs")
center_text(12)
center_text("spam spam spam spam")

center_text("first", "second", 3, 4, "spam", sep=':')
print()