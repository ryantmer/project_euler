import projecteuler

def euler14(start):
    """Finds the longest Collatz sequence starting from start."""
    longest_chain_length = 0
    longest_chain_idx = start

    for i in xrange(start, 0, -1):
        if i % 100000 == 0:
            print "Checking", i
        j = i
        chain_length = 0
        while j > 1:
            chain_length += 1
            if j % 2 == 0:
                j /= 2
            else:
                j = 3*j + 1
        if chain_length > longest_chain_length:
            longest_chain_length = chain_length
            longest_chain_idx = i

    return longest_chain_idx



# print euler14(27)
print euler14(1000000)