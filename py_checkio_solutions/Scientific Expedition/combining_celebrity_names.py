#!/usr/bin/env checkio --domain=py run combining-celebrity-names
def brangelina(first: str, second: str) -> str:
    vowels = 'aeiou'
    group_1, group_2 = [], []
    add_part = lambda p: group_1.append(p) if name == first else group_2.append(p)
    for name in (first, second):
        part = ''
        prev_char = ''
        for char in name:
            if char in vowels and not(prev_char and prev_char in vowels):
                add_part(part)
                part = ''
            part += char
            prev_char = char
        add_part(part)
    # len(group_*)-2(, -1 - difference index number and len seq, -1 - division word on groups before vowel and with it
    res = ''.join(group_1[:-2] if len(group_1) > 2 else group_1[:-1])
    res += ''.join(group_2[1:] if len(group_2) >= 2 else group_2[:])
    return res


print("Example:")
print(brangelina("angelina", "brad"))
print(brangelina("brad", "angelina"))
print(brangelina("sheldon", "amy"))

# These "asserts" are used for self-checking
assert brangelina("brad", "angelina") == "brangelina"
assert brangelina("angelina", "brad") == "angelad"
assert brangelina("sheldon", "amy") == "shamy"
assert brangelina('amy', 'sheldon') == 'eldon'
assert brangelina('britain', 'exit') == 'brexit'

print("The mission is done! Click 'Check Solution' to earn rewards!")
