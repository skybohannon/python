try:
    howMany = int(input("How many Fibonacci numbers would you like to generate? "))
    count = 1
    fibo = []

    if howMany == 0:
        fibo = []
    elif howMany == 1:
        fibo = [1]
    elif howMany == 2:
        fibo = [1, 1]
    elif howMany > 2:
        fibo = [1, 1]
        while count < (howMany - 1):
            fibo.append(fibo[count-1] + fibo[count])
            count += 1

    fiboString = ', '.join(str(x) for x in fibo)
    print("Your Fibonacci sequence is: " + fiboString)

except ValueError:
    print("You did not enter a number. You had one job.")
