#!/usr/bin/env checkio --domain=py run geometry-figures
from math import pi, sqrt


class Parameters:
    def __init__(self, side_r):
        self.side = side_r

    def choose_figure(self, figure):
        self.figure = figure
        figure.side = self.side

    def area(self):
        return self.figure.area()

    def perimeter(self):
        return self.figure.perimeter()

    def volume(self):
        return self.figure.volume()


class Circle:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return round(2 * pi * self.side, 2)

    def area(self):
        return round(pi * self.side ** 2, 2)

    def volume(self):
        return 0


class Triangle:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return round(3 * self.side, 2)

    def area(self):
        return round((sqrt(3) / 4) * (self.side ** 2), 2)

    def volume(self):
        return 0


class Square:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def volume(self):
        return 0


class Pentagon:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return self.side * 5

    def area(self):
        return round(sqrt(25 + 10 * sqrt(5)) / 4 * (self.side ** 2), 2)

    def volume(self):
        return 0


class Hexagon:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return self.side * 6

    def area(self):
        return round((3 * sqrt(3) / 2) * (self.side ** 2), 2)

    def volume(self):
        return 0


class Cube:
    def __init__(self):
        self.side = 0

    def perimeter(self):
        return self.side * 12

    def area(self):
        return self.side ** 2 * 6

    def volume(self):
        return self.side ** 3


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)
    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
