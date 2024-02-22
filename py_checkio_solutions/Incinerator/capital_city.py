#!/usr/bin/env checkio --domain=py run capital-city
def singleton(class_):
    _instances = {}

    def getinstance(*args, **kwargs):
        return _instances.setdefault(class_, class_(*args, **kwargs))

    return getinstance


@singleton
class Capital:
    def __init__(self, city_name: str):
        self.city_name = city_name

    def name(self) -> str:
        return self.city_name


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
