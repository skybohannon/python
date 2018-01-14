# Write a Python program to strip a set of characters from a string.

str1 = "FYI man, alright. You could sit at home, and do like absolutely nothing, and your name goes through like 17 computers a day. 1984? Yeah right, man. That's a typo. Orwell is here now. He's livin' large. We have no names, man. No names. We are nameless!"

def strip_chars(s, chars):
    return "".join(c for c in s if c not in chars)

print(strip_chars(str1, "aeiou"))
