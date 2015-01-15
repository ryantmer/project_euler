def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def euler20(n):
    """Finds the sum of the digits in n!"""
    factorial_n = factorial(n)
    digit_sum = 0
    while factorial_n > 0:
        digit_sum += factorial_n % 10
        factorial_n /= 10
    return digit_sum

print euler20(100)