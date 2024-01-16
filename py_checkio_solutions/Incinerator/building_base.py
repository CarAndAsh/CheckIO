#!/usr/bin/env checkio --domain=py run building-base
class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.sw_coords = (south, west)
        self.we_width = width_WE
        self.ns_width = width_NS
        self.h = height

    def corners(self):
        return {'north-west': (self.sw_coords[0]+self.ns_width, self.sw_coords[1]),
                'north-east': (self.sw_coords[0]+self.ns_width, self.sw_coords[1]+self.we_width),
                'south-west': (self.sw_coords[0], self.sw_coords[1]),
                'south-east': (self.sw_coords[0], self.sw_coords[1]+self.we_width)}

    def area(self):
        return self.we_width * self.ns_width

    def volume(self):
        return self.area() * self.h

    def __repr__(self):
        return f'Building({self.sw_coords[0]}, {self.sw_coords[1]}, {self.we_width}, {self.ns_width}, {self.h})'


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())


    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {
        "north-east": [4, 4],
        "south-east": [1, 4],
        "south-west": [1, 2],
        "north-west": [4, 2],
    }, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
