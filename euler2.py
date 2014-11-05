def euler2(max_value):
    """Find sum of even numbers in Fibonacci sequence up to max_value"""
    total = 0
    val1 = 1
    val2 = 2
    while val2 < max_value:
        if val1 % 2 == 0:
            total += val1
        if val2 % 2 == 0:
            total += val2

        val1 += val2
        val2 += val1

    return total

print euler2(4000000)