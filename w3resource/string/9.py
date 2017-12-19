# Write a Python program to remove the nth index character from a nonempty string.


def remove_nth(a, b):
    first_pt = a[:b]
    last_pt = a[b+1:]
    return first_pt + last_pt


print(remove_nth('yeah this is goin down', 5))
print(remove_nth('the quick brown fox jumped over the lazy dog', 11))