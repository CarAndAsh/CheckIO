#!/usr/bin/env checkio --domain=py run atbash-cipher
from string import ascii_uppercase as up, ascii_lowercase as low


def atbash(plaintext: str) -> str:
    return ''.join([(low[-low.index(symb)-1] if symb in low else up[-up.index(symb)-1]) if symb.isalpha() else symb for symb in plaintext])


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")
