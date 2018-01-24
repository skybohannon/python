# Write a Python program to split a string on the last occurrence of the delimiter.


def delimsplit(s, n):
    return s.rsplit(',', n)


print(delimsplit("c,a,l,c,u,l,a,t,o,r", 5))
