# userSentence = input("Please enter a sentence: ")
#
# sentenceList = userSentence.split()
# sentenceLength = len(sentenceList)
# counter = sentenceLength - 1
# newList = []
#
# while counter >= 0:
#     newList.append(sentenceList[counter])
#     counter -= 1
#
# newListString = ' '.join(str(x) for x in newList)
# print(newListString)

userSentence = input("Please enter a sentence: ")

newListString = ' '.join(userSentence.split()[::-1])
print(newListString)