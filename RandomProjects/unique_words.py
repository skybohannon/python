# Return a set of the words in text that occur exactly once.
# "The boy jumped over the other boy"
# {'jumped', 'other', 'over'}


def unique_words(s):
    word_set = set()
    sentence_list = s.lower().split(" ")
    d = dict.fromkeys(set(sentence_list), 0)

    for i in sentence_list:
        d[i] += 1

    for k, v in d.items():
        if v == 1:
            word_set.add(k)

    return word_set


userSentence = input("LET'S FIND SOME UNIQUE WORDS!\nPlease enter a sentence: ")
print(unique_words(userSentence))
