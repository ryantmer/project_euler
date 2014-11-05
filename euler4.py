def euler4(x):
    """Finds the largest palindrome number which is the product of two x-digit numbers."""
    def is_palindrome(number):
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        
        if digits == digits[::-1]:
            return True
        else:
            return False

    max_palindrome = 0
    for i in xrange(10 ** x):
        for j in xrange(10 ** x):
            if is_palindrome(i * j) and i * j > max_palindrome:
                max_palindrome = i * j
    return max_palindrome

print euler4(3)