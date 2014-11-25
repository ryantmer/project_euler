# one, two, three, ..., eighteen, nineteen
length_1_19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# twenty, thirty, ..., eighty, ninety
length_10_90 = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
length_hundred = 7
length_and = 3
length_thousand = 8

def euler17(start, stop):
    """Calculates number of letters to write out numbers start to stop... poorly."""
    total_length = 0
    for number in range(start, stop + 1):
        if number < 20:
            total_length += length_1_19[number]  # one, two, ...
        elif number < 100:
            total_length += length_10_90[number // 10]  # twenty, thirty, ...
            total_length += length_1_19[number % 10]  # one, two, ...
        elif number < 1000:
            total_length += length_1_19[number // 100]  # one, two, ...
            total_length += length_hundred  # hundred
            if number % 100 != 0:
                total_length += length_and  # and
            if number % 100 < 20:
                total_length += length_1_19[number % 100]
            else:
                total_length += length_10_90[number % 100 // 10]
                total_length += length_1_19[number % 100 % 10]
        else:
            total_length += length_1_19[number // 1000]
            total_length += length_thousand

    return total_length

print euler17(1, 1000)