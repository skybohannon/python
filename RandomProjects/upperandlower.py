def uplowcalc(sentence):

    d = {"UPPER": 0, "LOWER": 0}

    for c in sentence:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
        else:
            pass

    print("There were {} upper case characters".format(d["UPPER"]))
    print("There were {} lower case characters".format(d["LOWER"]))

sentence = input("Please enter a sentence")

uplowcalc(sentence)

# upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowerChars = "abcdefghijklmnopqrstuvwxyz"
#
# lowerCount = 0
# upperCount = 0
#
# sentence = input("Please enter a sentence: ")
#
# for x in sentence:
#     if x in upperChars:
#         upperCount += 1
#     if x in lowerChars:
#         lowerCount += 1
#
# print("Lower case characters: {}\nUpper case characters: {}".format(upperCount, lowerCount))