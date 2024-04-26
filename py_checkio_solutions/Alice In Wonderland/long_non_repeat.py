#!/usr/bin/env checkio --domain=py run long-non-repeat
def non_repeat(line: str) -> str:
    res = []
    for i, ch in enumerate(line):
        uniq_line = ch
        i += 1
        while i < len(line) and line[i] not in uniq_line:
            uniq_line += line[i]
            i += 1
        res.append(uniq_line)
    return max(res, key=len) if res else ''


print("Example:")
print(non_repeat("abdjwawk"))

# These "asserts" are used for self-checking
assert non_repeat("aaaaa") == "a"
assert non_repeat("abdjwawk") == "abdjw"
assert non_repeat("abcabcffab") == "abcf"
assert non_repeat('w') == 'w'
print("The mission is done! Click 'Check Solution' to earn rewards!")
