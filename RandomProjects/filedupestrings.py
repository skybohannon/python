happy = []  # make empty happy list
with open('happynumbers.txt', 'r') as happyFile:
    line = happyFile.readline()
    for word in happyFile:
        happy.append(int(word))
        happyFile.readline()

primes = []  # make empty primes list
with open('primenumbers.txt', 'r') as primesFile:
    line = primesFile.readline()
    for word in primesFile:
        primes.append(int(word))
        primesFile.readline()

matchingList = []  # make empty matching list
for number in primes:
    if number in happy:
        matchingList.append(number)

print("The matching numbers are: " + ", ".join(str(x) for x in matchingList))
