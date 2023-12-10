def factorial_integer(n):
    if n < 0:
        return "Silnia nie jest zdefiniowana dla liczb ujemnych"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def factorial_fractional(x):
    if x < 0:
        return "Silnia nie jest zdefiniowana dla liczb ujemnych"
    elif x == 0:
        return 1
    else:
        return math.gamma(x + 1)