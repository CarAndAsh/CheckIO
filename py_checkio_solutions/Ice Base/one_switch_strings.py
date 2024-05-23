#!/usr/bin/env checkio --domain=py run one-switch-strings
from collections import Counter


def switch_strings(line: str, result: str) -> bool:
    rem_ch = ''
    if Counter(line) == Counter(result):
        for i, (ch_1, ch_2) in enumerate(zip(line, result)):
            if ch_1 != ch_2 and (ch_1 == rem_ch if rem_ch else True):
                line = line[:i] + ch_2 + line[i+1:]
                if rem_ch:
                    return line == result
                rem_ch = ch_2
        return True
    return False


print("Example:")
print(switch_strings('adkglaigrbosudfbklabsdlkgalkkfndah', 'adkglaigrbosudfbllabsdlkgakkkfndah'))

# These "asserts" are used for self-checking
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True
assert switch_strings('adkglaigrbosudfbklabsdlkgalkkfndah', 'adkglaigrbosudfbllabsdlkgakkkfndah') == True
assert switch_strings("bopep", "bobep") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
