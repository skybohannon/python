# 39. Write a Python program to compute the future value of a specified principal amount,
# rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79


def future_value(amt, int, years):
    future = round(amt*((1+(0.01*int)) ** years),2)
    return "Principal: ${}\nRate of interest: {}\nYears: {}\nFuture value: ${}".format(amt, int, years, future)

print(future_value(10000, 3.5, 7))
