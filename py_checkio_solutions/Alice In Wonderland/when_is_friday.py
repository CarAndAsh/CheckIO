#!/usr/bin/env checkio --domain=py run when-is-friday
import datetime as dt


def friday(day: str) -> int:
    weekday = dt.date(*reversed(tuple(map(int, day.split('.'))))).weekday()
    return 4 - weekday if weekday <= 4 else 7 - (weekday - 4)


print("Example:")
print(friday("03.04.2024"))

assert friday("12.04.2018") == 1
assert friday("01.01.1999") == 0
assert friday('11.11.1111') == 6 
print("The mission is done! Click 'Check Solution' to earn rewards!")
