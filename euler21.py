import projecteuler

def euler21(n):
    """Finds sum of amicable numbers < n.

    Amicable numbers are numbers where d(a) = b and d(b) = a, where d(x) is 
    the sum of the proper divisors of x.
    """

    amicable_sum = 0

    for num in range(1, n):
        div_1 = projecteuler.proper_divisors(num)
        div_sum_1 = sum(div_1)
        div_2 = projecteuler.proper_divisors(div_sum_1)
        div_sum_2 = sum(div_2)
        if num == div_sum_2 and num != div_sum_1:
            amicable_sum += num

    return amicable_sum

print euler21(10000)