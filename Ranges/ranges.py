# myList = list(range(10))
# print(myList)
#
# even = list(range(0, 1000, 2))
# odd = list(range(1, 1000, 2))
#
# print(even)
# print(odd)
#
# range(0, 10)
# range(0, 10000)
#
# myString = "abcdefghijklmnopqrstuvwxyz"
# print(myString.index('e'))
# print(myString[4])
#
# smallDecimals = range(0,10)
# print(smallDecimals)
#
# print(smallDecimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[985])
#
# sevens = range(7, 10000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
#
# print(smallDecimals)
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))

decimals = range(0, 100)
print(decimals)

myRange = decimals[3:40:3]
print(myRange)

for i in myRange:
    print(i)

print('=' * 40)
for i in range(3, 40, 3):
    print(i)

print(myRange == range(3, 40, 3))