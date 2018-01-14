# 40. Write a Python program to reverse words in a string

str1 = "FYI man, alright. You could sit at home, and do like absolutely nothing, and your name goes through like 17 computers a day. 1984? Yeah right, man. That's a typo. Orwell is here now. He's livin' large. We have no names, man. No names. We are nameless!"

def reverse_words(s):
    for line in s.split('\n'):
        return(' '.join(line.split()[::-1]))

print(reverse_words(str1))