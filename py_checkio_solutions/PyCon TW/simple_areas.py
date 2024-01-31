#!/usr/bin/env checkio --domain=py run simple-areas
from functools import wraps
from math import pi, sqrt


def round_2(f):
    @wraps(f)
    def wrapper(*args):
        return round(f(args), 2)

    return wrapper


@round_2
def simple_areas(args):
    if not args:
        return 0
    elif len(args) == 1:
        return pi * (args[0] / 2) ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        p = sum(args) / 2
        return sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
    assert almost_equal(simple_areas(1, 1, 1), 0.43)
