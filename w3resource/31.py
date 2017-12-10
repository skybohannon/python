# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.


def gcd(i1, i2):
    gcd = 1

    if i1 % i2 == 0:
        return i2

    for k in range(int(i2 / 2), 0, -1):
        if i1 % k == 0 and i2 % k == 0:
            gcd = k
            break
    return gcd


print(gcd(12, 17))
print(gcd(11, 22))
