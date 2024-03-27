#!/usr/bin/env checkio --domain=py run multicolored-lamp
class Lamp:
    def __init__(self):
        self.lamp = YellowLamp()

    def light(self):
        self.lamp = self.lamp.switch()
        return self.lamp.color


class GreenLamp:
    def __init__(self):
        self.color = 'Green'

    def __repr__(self):
        return self.color

    def switch(self):
        return RedLamp()


class RedLamp:
    def __init__(self):
        self.color = 'Red'

    def __repr__(self):
        return self.color

    def switch(self):
        return BlueLamp()


class BlueLamp:
    def __init__(self):
        self.color = 'Blue'

    def __repr__(self):
        return self.color

    def switch(self):
        return YellowLamp()


class YellowLamp:
    def __init__(self):
        self.color = 'Yellow'

    def __repr__(self):
        return self.color

    def switch(self):
        return GreenLamp()


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()
    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
