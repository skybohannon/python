userSentence = input("Please enter a sentence: ")
wordList = [x for x in userSentence.split(" ")]
print(" ".join(sorted(set(wordList))))