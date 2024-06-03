#!/usr/bin/env checkio --domain=py run army-battles
# Taken from mission The Warriors

class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__(attack=7)


def fight(unit_1, unit_2):
    while unit_2.is_alive and unit_1.is_alive:
        unit_2.health -= unit_1.attack
        unit_1.health -= unit_2.attack if unit_2.is_alive else 0
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, amount):
        [self.units.insert(0, unit_class()) for _ in range(amount)]


class Battle:
    def fight(self, army_1, army_2):
        while army_1.units and army_2.units:
            fight(army_1.units[-1], army_2.units[-1])
            army_1.units.pop() if army_2.units[-1].is_alive else army_2.units.pop()
        return bool(army_1.units)
    

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
