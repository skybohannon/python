def findperfect(n):

    # find divisors
    userNumberRange = list(range(1, n+1))
    divisors = []

    for num in userNumberRange:
        if n % num == 0:
            divisors.append(num)

    # see if number is perfect
    perfects = 0
    for num in divisors[:-1]:
        perfects += num

    if perfects == n:
        print("{} is a perfect number".format(n))
    else:
        print("{} isn't a perfect number".format(n))
try:
    userNumber = int(input("Please enter a number: "))
    findperfect(userNumber)
except ValueError:
    print("You didn't enter a number")


# def findperfects(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += n
#     return sum != n
#
# print(findperfects(6))
