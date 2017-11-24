# # Pick words of certain length from a string, but ignore punctuation
#
#
# def find_words_of_length(number, text):
#     """ Remove punctuation from text, then return words of length number.
#
#     >>> find_words_of_length(4, "this is a string with some four-letter words.")
#     >>> ['this', 'with', 'some']

length = 4
s = "this is a strange with some four-letter words."


def find_words_of_length(lgth, str):
    out = "".join(c for c in str if c not in ('!', '?', '.', ':'))
    s_list = out.split(" ")
    correct_length = []
    for word in s_list:
        if len(word) == lgth:
            correct_length.append(word)

    return correct_length


print(find_words_of_length(length, s))
