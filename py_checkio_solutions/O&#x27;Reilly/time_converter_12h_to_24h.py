#!/usr/bin/env checkio --domain=py run time-converter-12h-to-24h
def time_converter(time):
    time, day_part = time.split()
    hour, minutes = time.split(':')
    if hour == '12':
        hour = f'{int(hour) if day_part == "p.m." else 0}'
    elif day_part == 'p.m.':
        hour = f'{int(hour) + 12}'
    return f'{hour.zfill(2)}:{minutes}'


if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("12:30 a.m.") == "00:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print("Coding complete? Click 'Check' to earn cool rewards!")
