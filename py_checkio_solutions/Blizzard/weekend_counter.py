#!/usr/bin/env checkio --domain=py run weekend-counter
from datetime import date, timedelta


def checkio(from_date, to_date):
    """
    Count the days of rest
    """
    с = 0
    while from_date <= to_date:
        if from_date.weekday() in (5,6):
            с += 1
        from_date = from_date + timedelta(1)
    return с


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
