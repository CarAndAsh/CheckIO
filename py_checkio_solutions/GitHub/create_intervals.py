#!/usr/bin/env checkio --domain=py run create-intervals
def create_intervals(data:set):
    res = []
    first = None
    while data:
        el = min(data)
        data.remove(el)
        if not first:
            first = el
        if first and (not data or (min(data)-el) > 1):
            res.append((first, el))
            first = None
    return res


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals({8, 7}) == [(7, 8)]
    print("Almost done! The only thing left to do is to Check it!")
