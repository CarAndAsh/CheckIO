#!/usr/bin/env checkio --domain=py run the-vampires
# Taken from mission The Defenders
# Taken from mission Army Battles
# Taken from mission The Warriors
class Warrior:
    def __init__(self, health=50, attack=5, defense=0, vampirism=0):
        self.health = health
        self.max_hp = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism / 100

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        if isinstance(other, Warrior):
            other.health -= dmg if (dmg := (self.attack - other.defense)) > 0 else 0

        if isinstance(self, Vampire):
            vamp = ((self.attack - other.defense) * self.vampirism)
            self.health = (self.health + vamp) if (self.max_hp - self.health) > vamp else self.max_hp


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__(health=60, attack=3, defense=2)


class Vampire(Warrior):
    def __init__(self):
        super(Vampire, self).__init__(health=40, attack=4, vampirism=50)


def fight(unit_1, unit_2):
    while unit_2.is_alive and unit_1.is_alive:
        unit_1.hit(unit_2)
        if unit_2.is_alive:
            unit_2.hit(unit_1)
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
