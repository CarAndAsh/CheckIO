#!/usr/bin/env checkio --domain=py run secret-message
def find_message(message: str) -> str:
    if message:
        res = ''
        for ch in message:
            if ch.isupper():
                res += ch
        return res
    return ''


if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
