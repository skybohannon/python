userNumber = int(input("Please enter a number to find all divisors for: "))
userNumberRange = list(range(1, userNumber+1))
divisors = []

for num in userNumberRange:
    if userNumber % num == 0:
        divisors.append(num)

print(divisors)