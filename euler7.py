import projecteuler

def euler7(n):
    """Finds the n-th prime number."""
    curr_prime_index = 0
    curr_number = 2
    while True:
        if projecteuler.is_prime(curr_number):
            curr_prime_index += 1
        if curr_prime_index >= n:
            return curr_number
        curr_number += 1

print euler7(10001)