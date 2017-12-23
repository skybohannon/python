# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
# Click me to see the sample solution


def reverse_if_4(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return "Not divisible by 4"


print(reverse_if_4('Word'))
print(reverse_if_4('Hello'))
