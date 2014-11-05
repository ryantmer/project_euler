def euler3(value):
    """Find largest prime factor of value."""
    N = n = value
    p = 2

    while p ** 2 <= n:
        if n % p == 0:
            n //= p
        else:
            if p > 2:
                p += 2
            else:
                p += 1

    return n

print euler3(600851475143)