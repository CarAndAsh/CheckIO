#!/usr/bin/env checkio --domain=py run completely-empty
from collections.abc import Iterable


def completely_empty(val):
    return all(('__iter__' in i.__dir__() if isinstance(i, Iterable) else False) and completely_empty(i) for i in val)




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[], []]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[], [1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[], [{'': 'No WAY'}]]) == True
    assert completely_empty([type('', (), {'__iter__': None})()]) == False, 'Extra 4'
    assert completely_empty(type('', (), {'__getitem__': ().__getitem__})()) == True, 'Extra 5'
    print('Done')
