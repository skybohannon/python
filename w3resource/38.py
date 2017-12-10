# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


def solveit(a, b):
    return "The result of ({} + {}) * ({} + {}) is {}".format(a, b, a, b, (a + b) * (a + b))


print(solveit(4, 3)
