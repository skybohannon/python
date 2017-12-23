# 24. Write a Python program to check whether a string starts with specified characters.



def check_str(s, chars):
    if s[:(len(chars))] == chars:
        return True
    else:
        return False


def check_str2(s, chars):
    if s.startswith(chars):
        return True
    else:
        return False

print(check_str('The quick brown fox', 'Th'))
print(check_str('The quick brown fox', 'Tge'))

print(check_str2('The quick brown fox', 'Th'))
print(check_str2('The quick brown fox', 'Tge'))