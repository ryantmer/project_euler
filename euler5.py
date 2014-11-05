import projecteuler

def euler5(x):
    """Finds smallest positive number evenly divisible by all numbers from 1 to x."""
    # Multiply all numbers from 1 to x to start, and work down from here
    current = reduce(lambda a, b: a*b, range(1, x + 1))

    x_to_1 = range(x, 0, -1)
    divisors = range(x, 0, -1)

    for i in range(x, 0, -1):
        if projecteuler.is_divisible(current // i, x_to_1):
            current //= i
            divisors.pop(divisors.index(i))

    return current

print euler5(20)