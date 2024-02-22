#!/usr/bin/env checkio --domain=py run unix-match
import re


def unix_match(filename: str, pattern: str) -> bool:
    if set(filename) == set(pattern):
        return True
    if any(map(lambda char: char.isalnum(), filename)):
        pattern = pattern.replace("*", "\S*")\
            .replace(".", "\\.")\
            .replace("[!", "[^")\
            .replace('?', '\S{1}')\
            .replace('[]', '[^.]')
    return bool(re.match(pattern, filename))


if __name__ == '__main__':
    print("Example:")
    print(unix_match("apatche121.log", "*[1234567890].*"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("apache12.log", "*[1234567890].*") == True
    assert unix_match("name.txt", "name[.]txt") == True
    assert unix_match("apache.12log", "*[1234567890].*") == False
    assert unix_match("name....", "name.[!.][!.][!.]") == False
    assert unix_match("name.exe", "name.[!.][!.][!.]") == True
    assert unix_match('txt', '????*') == False
    assert unix_match('l.txt', '???*') == True
    assert unix_match("[?*]", "[[][?][*][]]") == True
    assert unix_match("name.txt", "name[]txt") == False
    assert unix_match("[!]check.txt", "[!]check.txt") == True

    print("Coding complete? Click 'Check' to earn cool rewards!")
