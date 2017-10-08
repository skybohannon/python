# age = int(input("How old are you? "))
# if not (age < 18):
#     print("You are old enough to vote")
# else:
#     print("Please come back in {} years".format(18-age))

parrot = "Norwegian Blue"

letter = input("Please input a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter.")