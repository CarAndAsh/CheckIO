#!/usr/bin/env checkio --domain=py run army-battles
# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_2.is_alive and unit_1.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
        else:
            return True
    return False


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, unit_class, amount):
        [self.army.append(unit_class()) for _ in range(amount)]


class Battle:
    def fight(self, army_1, army_2):
        fighter_1 = army_1.army.pop(0)
        fighter_2 = army_2.army.pop(0)
        while (fighter_1.is_alive or army_1.army) and (fighter_2.is_alive or army_2.army):
            if not fighter_1.is_alive:
                fighter_1 = army_1.army.pop(0)
            if not fighter_2.is_alive:
                fighter_2 = army_2.army.pop(0)
            fight(fighter_1, fighter_2)
        return bool(army_1.army or fighter_1.is_alive)


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
    
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 10)
    army_2.add_units(Warrior, 11)

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    assert battle.fight(army_1, army_2) == True

    print("Coding complete? Let's try tests!")
