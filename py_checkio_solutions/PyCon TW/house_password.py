#!/usr/bin/env checkio --domain=py run house-password
def checkio(data: str) -> bool:
    flag_upper = False
    flag_lower = False
    flag_num = False
    flag_alnum = True
    flag_len = False
    for i, char in enumerate(data, 1):
        if char.isupper():
            flag_upper = True
        if char.islower():
            flag_lower = True
        if char.isdigit():
            flag_num = True
        if not char.isalnum():
            flag_alnum = False
        if i >= 10:
            flag_len = True
    return all((flag_alnum, flag_num, flag_upper, flag_len, flag_lower))


print("Example:")
print(checkio("A1213pokl"))

# These "asserts" are used for self-checking
assert checkio("ULFFunH8ni") == True
assert checkio("aaaaaaaaaaaaaaaaaaaaa") == False
assert checkio("aA1") == False
assert checkio("awzbdzkfz") == False
assert checkio("RCAGOSHTTS") == False
assert checkio("6691219721") == False
assert checkio("PVlppfwrT") == False
assert checkio("45ae5lkgz") == False
assert checkio("1cmuPF1Ycz") == True
assert checkio("Pv4HdnUNb") == False
assert checkio("jRNfXg6CdM15SLChALq") == True
assert checkio("HZeLrcRR3NU5KprAybp") == True
assert checkio("aaaaaaaaaa1A") == True
assert checkio("aaaaaaaaa1Za") == True
assert checkio("aaaaaaaaa9Aa") == True
assert checkio("AAAAAAAAA1zA") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
