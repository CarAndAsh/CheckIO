#!/usr/bin/env checkio --domain=py run calculator-i
def calculator(log: str) -> str:
    first = ''
    second = ''
    action = ''
    for ch in log:
        if ch.isdigit():
            if not action:
                if not first and ch == '0':
                    continue
                else:
                    first += ch
            else:
                if not second and ch == '0':
                    continue
                else:
                    second += ch
        else:
            if first and action and second:
                first = str(eval(first + action + second))
                second = ''
                action = ch
            if ch == '-':
                if not first:
                    first += ch
                else:
                    action = ch

            elif ch == '+':
                if first:
                    action = ch
            elif ch == '=':
                if not action and not second:
                    first = ''
    return second if action and second and log[-1] not in ('=', '-') else first or '0'


print("Example:")
print(calculator("00012"))

# These "asserts" are used for self-checking
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"
assert calculator('-5-10+15-') == '0'
print("The mission is done! Click 'Check Solution' to earn rewards!")
