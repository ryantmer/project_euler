import itertools
import math

def euler24(n, digits):
    """Finds the n-th lexicographic permutation of [digits]."""
    permutations = [x for x in itertools.permutations(digits, len(digits))]
    return permutations[n-1]

def euler24alt(n, digits):
    """Finds the n-th lexicographic permutation of [digits] using Euler. Much faster."""
    permutation = []

    n -= 1

    for i in range(len(digits)-1, -1, -1):
        index = n / math.factorial(i)
        permutation.append(digits[index])
        del digits[index]
        n -= index * math.factorial(i)

    return permutation

print euler24(1000000, [0,1,2,3,4,5,6,7,8,9])
print euler24alt(1000000, [0,1,2,3,4,5,6,7,8,9])