#!/usr/bin/env checkio --domain=py run the-most-frequent-weekdays
from calendar import Calendar


def most_frequent_days(year):
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    clndr = Calendar()
    first_week = clndr.yeardayscalendar(year)[0][0][0]
    last_week = clndr.yeardayscalendar(year)[-1][-1][-1]
    if sum((first_week.count(0), last_week.count(0))) > 7:
        mask = list(map(lambda x: bool(first_week[x] or last_week[x]), range(7)))
    else:
        mask = list(map(lambda x: bool(first_week[x] and last_week[x]), range(7)))
    return list(i[0] for i in filter(lambda x: x[1], zip(weekdays, mask)))


if __name__ == "__main__":
    print("Example:")
    print(most_frequent_days(328))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ["Tuesday", "Wednesday"]
    assert most_frequent_days(1167) == ["Sunday"]
    assert most_frequent_days(1216) == ["Friday", "Saturday"]
    assert most_frequent_days(1492) == ["Friday", "Saturday"]
    assert most_frequent_days(1770) == ["Monday"]
    assert most_frequent_days(1785) == ["Saturday"]
    assert most_frequent_days(212) == ["Wednesday", "Thursday"]
    assert most_frequent_days(1) == ["Monday"]
    assert most_frequent_days(2135) == ["Saturday"]
    assert most_frequent_days(3043) == ["Sunday"]
    assert most_frequent_days(2001) == ["Monday"]
    assert most_frequent_days(3150) == ["Sunday"]
    assert most_frequent_days(3230) == ["Tuesday"]
    assert most_frequent_days(328) == ["Monday", "Sunday"]
    assert most_frequent_days(2016) == ["Friday", "Saturday"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
