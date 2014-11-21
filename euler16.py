def euler16(n):
    """Finds the sum of the digits of the value of 2 ** n."""
    exp_val = 2**n
    exp_str = str(exp_val)

    exp_sum = 0
    for digit in exp_str:
        exp_sum += int(digit)
    return exp_sum

print euler16(1000)