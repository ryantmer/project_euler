def euler1(max_value):
    """Find sum of all multiples of 3 or 5 below max_value"""
    total = 0

    for i in xrange(max_value):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

print euler1(1000)