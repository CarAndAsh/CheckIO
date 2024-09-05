#!/usr/bin/env checkio --domain=py run reveal-the-number
def reveal_num(line: str) -> int | float | None:
    first_dot = True
    sign = ''
    res = ''
    for ch in line:
        if first_dot:
            if ch == '.' and res:
                res += '.'
                first_dot = False
            elif ch == '-' and not res:
                sign = '-'
            elif ch == '+' and not res:
                sign = ''
        if ch.isnumeric():
            res += ch
    print(sign + (res[:-1] if res[-1] == '.' else res) if res else None)
    return float(sign + res) if '.' in res and res.index('.') != len(res) - 1 else (int(sign + res[:-1]) if res[-1] == '.' else int(sign + res)) if res else None


print("Example:")
print(reveal_num("+A%+-1-0..."))

# These "asserts" are used for self-checking
assert reveal_num("F0(t}") == 0
assert reveal_num("Utc&g") == None
assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
assert reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459
assert reveal_num('J-8:Z0') == -80
print("The mission is done! Click 'Check Solution' to earn rewards!")
