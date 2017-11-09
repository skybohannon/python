# Return a set of the words in text that occur exactly once.
# {'jumped', 'other', 'over'}

sentence = "The boy jumped over the other boy"


def unique_words(s):
    word_set = set()
    sentence_list = s.lower().split(" ")
    d = dict.fromkeys(set(sentence_list), 0)

    for i in sentence_list:
        d[i] += 1

    for k, v in d.items():
        if v <= 1:
            word_set.add(k)

    return word_set


print(unique_words(sentence))
