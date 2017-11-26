# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
#
# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True


def near_ten(num):
    within = num % ((num / 10) * 10) if num >= 10 else num
    return within in [8, 9, 0, 1, 2]


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
