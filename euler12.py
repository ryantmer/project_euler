import projecteuler

def euler12(num):
    """Finds the first triangle number to have over num divisors."""
    curr_number = 1
    increment = 1
    divisors = projecteuler.find_divisors(curr_number)

    while len(divisors) < num:
        increment += 1
        curr_number += increment
        divisors = projecteuler.find_divisors(curr_number)

    return curr_number

print euler12(500)