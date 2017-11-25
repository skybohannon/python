# # The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example,
#  the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the
# HTML string with tags around the word, e.g. "<i>Yay</i>".
#
#
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'


def make_tags(tag, s):
    new_string = "<{}>".format(tag) + s + "</{}>".format(tag)
    return new_string


user_tag = input("Please enter the tag you would like to use: ")
user_word = input("Please enter your word: ")
print(make_tags(user_tag, user_word))
