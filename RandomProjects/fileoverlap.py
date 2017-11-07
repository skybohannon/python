# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers
# up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers
# are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example,
# which I will describe below.)

primes = []  # make empty happy list
with open('primenumbers.txt', 'r') as primeFile:
    line = primeFile.readline()
    for word in primeFile:
        primes.append(int(word))
        primeFile.readline()

happies = []  # make empty happy list
with open('happynumbers.txt', 'r') as happyFile:
    line = happyFile.readline()
    for word in happyFile:
        happies.append(int(word))
        happyFile.readline()

overlaps = []
for i in primes:
    if i in happies:
        overlaps.append(i)

print(", ".join(str(x) for x in overlaps))
