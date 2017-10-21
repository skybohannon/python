sentence = input("Please enter a palindrome: ")

sentenceReversed = sentence[::-1]

if sentenceReversed == sentence:
    print("This is a palindrome!")
else:
    print("This isn't a palindrome.")
