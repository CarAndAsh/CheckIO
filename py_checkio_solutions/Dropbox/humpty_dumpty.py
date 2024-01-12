#!/usr/bin/env checkio --domain=py run humpty-dumpty
from math import pi, acos, sin, cos, e, log


def checkio(height, width):
    h, r = height / 2, width / 2
    if r < h:
        acs = acos(r / h)
        square = 2 * pi * ((r ** 2) + ((r * h * acs) / (sin(acs))))
    elif r > h:
        acs = acos(h / r)
        square = 2 * pi * ((r ** 2) + ((h ** 2) / (sin(acs))) * log(((1 + sin(acs)) / cos(acs)), e))
    else:
        square = 4 * pi * (r ** 2)
    volume = (4 * pi * (r ** 2) * h) / 3

    return [round(volume, 2), round(square, 2)]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
