def euler6(x):
    """Finds (square of sum) - (sum of squares) for first x natural numbers."""
    numbers = xrange(x + 1)

    sum_of_squares = 0
    for number in numbers:
        sum_of_squares += number ** 2

    square_of_sum = sum(numbers) ** 2

    return square_of_sum - sum_of_squares

print euler6(100)