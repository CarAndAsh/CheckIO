#!/usr/bin/env checkio --domain=py run the-first-working-day
from datetime import datetime as dt, timedelta as td


def vacation(date, days):
    day_after = dt.fromisoformat(date)+td(days=days)
    while day_after.weekday() not in range(0,5):
        day_after += td(1)
    return str(day_after.date())


if __name__ == "__main__":
    print("Example:")
    print(vacation("2018-07-01", 14))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation("2018-07-01", 14) == "2018-07-16"
    assert vacation("2018-02-19", 10) == "2018-03-01"
    assert vacation("2000-02-28", 5) == "2000-03-06"
    assert vacation("1999-12-20", 14) == "2000-01-03"
    print("Coding complete? Click 'Check' to earn cool rewards!")
