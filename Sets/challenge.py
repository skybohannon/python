# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

textInput = input("Please enter a short sentence: ")
vowels = frozenset("aeiou")

finalSet = set(textInput).difference(vowels)
print(finalSet)

sortedSet = sorted(finalSet)
print(sortedSet)