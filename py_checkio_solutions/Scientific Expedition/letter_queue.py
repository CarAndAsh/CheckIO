#!/usr/bin/env checkio --domain=py run letter-queue
from typing import List

def letter_queue(commands: List[str]) -> str:
    deque = ''
    for cmnd in commands:
        if cmnd.startswith('PUSH'):
            deque += cmnd.split()[-1]
        elif cmnd == 'POP':
            if deque:
                deque = deque[1:]
    return deque


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
