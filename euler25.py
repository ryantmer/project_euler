def fast_doubling_fibonacci(n):
    """Uses fast doubling algorithm to find F(n).

    See http://www.nayuki.io/page/fast-fibonacci-algorithms for more details.
    """

    if n <= 2:
        return 1
    else:
        a = fast_doubling_fibonacci(n / 2 + 1)
        b = fast_doubling_fibonacci(n / 2)
        if n % 2 == 1:
            return a*a + b*b
        else:
            return b*(2*a-b)

def euler25(n):
    """Finds the first term in the Fibonacci sequence that contains n digits."""
    i = 0
    fib = fast_doubling_fibonacci(i)
    while len(str(fib)) < n:
        i += 1
        fib = fast_doubling_fibonacci(i)
    return i, fib

print euler25(1000)