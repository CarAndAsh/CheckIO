#!/usr/bin/env checkio --domain=py run armstrong-number-checking
def is_armstrong(num: int) -> bool:
    str_num = str(num)
    return num == sum(map(lambda dig: int(dig) ** len(str_num), str_num))


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
