# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]
parrotList.append("A Norwegian Blue")

for state in parrotList:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbersSorted = sorted(numbers)
print(sorted(numbers))

if numbers == numbersSorted:
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbersSorted == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")