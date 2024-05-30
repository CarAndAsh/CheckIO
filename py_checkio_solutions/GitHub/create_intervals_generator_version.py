#!/usr/bin/env checkio --domain=py run create-intervals-generator-version
# Taken from mission Create Intervals

def create_intervals(data: set):
    first = None
    while data:
        el = min(data)
        data.remove(el)
        if not first:
            first = el
        if first and (not data or (min(data) - el) > 1):
            yield (first, el)
            first = None



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(create_intervals({1, 2, 3, 4, 5, 7, 8, 12})) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert list(create_intervals({1, 2, 3, 6, 7, 8, 4, 5})) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")
