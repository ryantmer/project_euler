# number of days per month in a non-leap year
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def euler19():
    """Calculates number of Sundays that were on the first day of the month from 1/1/1901 to 31/12/2000."""
    # 1 Jan 1900 was a Monday
    # Monday is 0th day of week, Tuesday is 1st, ..., Sunday is 6th day of week
    day_index = 0
    sundays = 0
    for year in range(1901, 2001):
        for month_length in month_days:
            day_index += month_length
            if month_length == 28:
                if year % 4 == 0:
                    if year % 400 == 0:
                        day_index += 1  # Add one day for leap years
                    else:
                        pass  # No leap years on centuries, except years divisible by 400
            if day_index % 7 == 6:
                sundays += 1
        print "Year:", year, "sundays:", sundays

    print sundays

euler19()