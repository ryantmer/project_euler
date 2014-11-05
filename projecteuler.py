import math

##### Helper functions #####
def is_divisible(number, values):
    """Returns True if number is evenly divisible by all values in [values]."""
    for i in values:
        if number % i != 0:
            return False
    return True

def is_prime(number):
    """Returns True if number is prime."""
    p = 2
    sqrt = math.sqrt(number)
    while p <= sqrt:
        if number % p == 0:
            return False
        if p > 2:
            p += 2
        else:
            p += 1
    return True

def find_divisors(number):
    """Returns a list of factors of number."""
    return reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0))
##### Helper functions #####