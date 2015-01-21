def cycle_length(number):
    """Finds the repeating cycle length of 1/number based on Euler."""
    if number % 2 == 0:
        return cycle_length(number / 2)
    if number % 5 == 0:
        return cycle_length(number / 5)

    i = 1
    while True:
        if (pow(10, i) - 1) % number == 0:
            return i
        i += 1

def euler26(d):
    """Finds i < d for which 1/i has the longest recurring cycle in its decimal fraction part."""
    max_cycle = 0
    max_cycle_denominator = 0

    for i in range(1, d):
        length = cycle_length(i)
        if length > max_cycle:
            max_cycle = length
            max_cycle_denominator = i

    return "1/{0} has the max cycle, with a length of {1}".format(max_cycle_denominator, max_cycle)

print euler26(1000)