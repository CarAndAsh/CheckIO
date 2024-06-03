#!/usr/bin/env checkio --domain=py run the-healers
# Taken from mission The Lancers
# Taken from mission The Vampires
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

    def hit(self, enemy, self_army, enemy_army):
        if isinstance(enemy, Warrior):
            enemy.health -= dmg if (dmg := (self.attack - enemy.defense)) > 0 else 0
        if enemy_army and isinstance(self, Lancer):
            enemy_army[-1].health -= dmg * 0.5
        if isinstance(self, Vampire):
            vamp = ((self.attack - enemy.defense) * self.vampirism)
            self.health = (self.health + vamp) if (self.max_hp - self.health) > vamp else self.max_hp
        if self_army and isinstance(self_army[-1], Healer):
            self_army[-1].heal(self)


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__(health=60, attack=3, defense=2)


class Vampire(Warrior):
    def __init__(self):
        super(Vampire, self).__init__(health=40, attack=4, vampirism=50)


class Lancer(Warrior):
    def __init__(self):
        super(Lancer, self).__init__(health=50, attack=6)


class Healer(Warrior):
    def __init__(self):
        super(Healer, self).__init__(health=60, attack=0)

    def heal(self, unit):
        unit.health = (unit.health + 2) if (unit.max_hp - unit.health) > 2 else unit.max_hp


def fight(unit_1, unit_2, army_1=None, army_2=None):
    while unit_2.is_alive and unit_1.is_alive:
        if army_2 and not army_2[-1].is_alive:
            army_2.pop()
        unit_1.hit(unit_2, army_1, army_2)
        if unit_2.is_alive:
            if army_1 and not army_1[-1].is_alive:
                army_1.pop()
            unit_2.hit(unit_1, army_2, army_1)
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, amount):
        [self.units.insert(0, unit_class()) for _ in range(amount)]


class Battle:
    def fight(self, army_1, army_2):
        while army_1.units and army_2.units:
            fight(army_1.units[-1], army_2.units[-1], army_1.units[:-1], army_2.units[:-1])
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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
