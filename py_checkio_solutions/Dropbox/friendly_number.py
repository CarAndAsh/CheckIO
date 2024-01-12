#!/usr/bin/env checkio --domain=py run friendly-number
def friendly_number(number: int, options: dict) -> str:
    base = options.get('base') or 1000
    decimals = options.get('decimals') or 0
    powers = options.get('powers') or ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    suffix = options.get('suffix') or ''
    i = 0
    while divmod(abs(number), (base ** i))[0] != 0 and i != len(powers):  # to find power
        i += 1
    i -= 1 if i > 0 else 0
    num = number / (base ** i) if decimals != 0 else int(number / (base ** i))
    res = str(f'{num:.{decimals}f}') + powers[i] + suffix
    return res


print("Example:")
print(friendly_number(102, {}))

# These "asserts" are used for self-checking
assert friendly_number(102, {}) == "102"
assert friendly_number(12341234, {"decimals": 1}) == "12.3M"
assert friendly_number(12000000, {"decimals": 3}) == "12.000M"
assert friendly_number(102, {"decimals": 2}) == "102.00"
assert friendly_number(10240, {}) == "10k"
assert friendly_number(1024000000, {"base": 1024, "suffix": "iB"}) == "976MiB"
assert friendly_number(-150, {"base": 100, "powers": ["", "d", "D"]}) == "-1d"
assert friendly_number(-155, {"base": 100, "decimals": 1, "powers": ["", "d", "D"]}) == "-1.6d"
assert friendly_number(255000000000, {"powers": ["", "k", "M"]}) == "255000M"
assert friendly_number(0, {'decimals': 3, 'suffix': 'th'}) == '0.000th'

print("The mission is done! Click 'Check Solution' to earn rewards!")
