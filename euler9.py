def euler9(num):
    """Find the product of a*b*c s.t. a < b < c, a**2 + b**2 = c**2, and a + b + c = num"""
    for a in range(1, num / 2):
        for b in range(a + 1, num / 2):
            for c in range(b + 1, num / 2):
                # print "Checking a =", a, "b =", b, "c =", c
                if a**2 + b**2 == c**2:
                    if a + b + c == num:
                        return a*b*c

print euler9(1000)