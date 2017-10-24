def get_number():
    return int(input("Please enter a number: "))

try:
    userNumber = get_number()

    userNumberRange = list(range(1, userNumber+1))
    divisors = []

    for num in userNumberRange:
        if userNumber % num == 0:
            divisors.append(num)

    if len(divisors) == 2:
        print("{} was a prime number!".format(userNumber))
    else:
        divisorsString = ', '.join(str(x) for x in divisors)
        print("{} wasn't prime. It's divisors are {}".format(userNumber, divisorsString))

except ValueError:
    print("You did not enter a number. You had one job.")
