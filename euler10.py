import projecteuler

def euler10(num):
    """Finds the sum of all primes below num."""
    total = 0
    curr_number = 2
    while curr_number < num:
        if projecteuler.is_prime(curr_number):
            total += curr_number
        curr_number += 1
    return total

print euler10(2000000)