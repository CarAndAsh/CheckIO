#!/usr/bin/env checkio --domain=py run time-converter-24h-to-12h
def time_converter(time: str) -> str:
    # replace this for solution
    if time:
        hours = int(time[:2])
        if hours > 12:
            return str(hours - 12) + time[2:] + ' ' + 'p.m.'
        elif hours == 12:
            return str(hours) + time[2:] + ' ' + 'p.m.'
        elif hours in (0, 24):
            return '12' + time[2:] + ' ' + 'a.m.'
        else:
            return str(hours) + time[2:] + ' ' + 'a.m.'
    return ""


print("Example:")
print(time_converter("12:30"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

print("The mission is done! Click 'Check Solution' to earn rewards!")
