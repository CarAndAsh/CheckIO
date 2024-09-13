#!/usr/bin/env checkio --domain=py run minimum-window-substring
def window(line: str, pattern: str) -> tuple[int, int]:
    sub_borders_list = []
    while all(map(lambda ch: ch in line, pattern)):
        ind_lst = list(map(lambda ch: line.rindex(ch), pattern))
        line = line[:max(ind_lst)]
        sub_borders_list.append((min(ind_lst), max(ind_lst) + 1))
        sub_borders_list.sort()
    return min(sub_borders_list, key=lambda x: x[1] - x[0]) if sub_borders_list else (-1, -1)


print("Example:")
print(window("ADOBECODEBANC", "ABC"))

# These "asserts" are used for self-checking
assert window("ADOBECODEBANC", "ABC") == (9, 13)
assert window("ab", "a") == (0, 1)
assert window("ab", "A") == (-1, -1)
assert window("abcdef", "ace") == (0, 5)
assert window("MixEdCaSeScRiNgTrIcKy", "cSeR") == (8, 12)
assert window('aa', 'a') == (0, 1)

print("The mission is done! Click 'Check Solution' to earn rewards!")
