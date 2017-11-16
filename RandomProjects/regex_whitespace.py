# Use regex to eliminate whitespace(s) between two specific words
import re

sentence = "an app store app maker app    store"
print(re.sub(r"\b(app)\s+([a-z])", r"\1\2", sentence))

# def remove_spaces(text, word_one, word_two):
