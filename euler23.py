import projecteuler as pe

def is_abundant(number):
    if number < 12:
        return False
    else:
        return sum(pe.proper_divisors(number)) > number

def euler23(number):
    """Finds sum of all pos ints which cannot be written as the sum of two abundant numbers.

    Abundant numbers are numbers where sum(divisors(x)) > x. All ints greater than 28193 are 
    known to be able to be expressed as the sum of abundant numbers, so this is our limit.
    """

    abundant_numbers = set(i for i in range(1, number + 1) if is_abundant(i))

    def abundant_sum(i):
        return any((i - a) in abundant_numbers for a in abundant_numbers)

    return sum(i for i in range(1, number + 1) if not abundant_sum(i))

print euler23(28123)