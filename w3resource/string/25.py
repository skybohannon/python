# 25. Write a Python program to create a Caesar encryption. Go to the editor
#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code
# or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution
# cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after
# Julius Caesar, who used it in his private correspondence.

low_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
up_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
crypted = []

def caesar(s, move):
    for char in s:
        if char in up_alph:
            index = up_alph.index(char)
            crypting = (index + move) % 26
            crypted.append(crypting)
        return crypted


print(caesar('Xyz', 2))
