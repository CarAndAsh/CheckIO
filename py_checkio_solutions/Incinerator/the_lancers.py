#!/usr/bin/env checkio --domain=py run the-lancers
# Taken from mission The Vampires
# Taken from mission The Defenders
# Taken from mission Army Battles
# Taken from mission The Warriors
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super(Vampire, self).__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Lancer(Warrior):
    def __init__(self):
        super(Lancer, self).__init__()
        self.health = 50
        self.attack = 6


def fight(unit_1, unit_2, army_1=None, army_2=None):
    if isinstance(unit_1, Vampire):
        health_limit = unit_1.health
    elif isinstance(unit_2, Vampire):
        health_limit = unit_2.health
    while unit_2.is_alive and unit_1.is_alive:
        damage = unit_1.attack - unit_2.defense
        unit_2.health -= damage if damage > 0 else 0
        if isinstance(unit_1, Lancer) and army_2 and army_2.army:
            army_2.army[0].health -= damage / 2
        if unit_1.vampirism and unit_1.health < health_limit:
            unit_1.health += damage / 100 * unit_1.vampirism

        if unit_2.is_alive:
            damage = unit_2.attack - unit_1.defense
            unit_1.health -= damage if damage > 0 else 0
            if isinstance(unit_2, Lancer) and army_1 and army_1.army:
                army_1.army[0].health -= damage / 2
            if unit_1.is_alive:
                if unit_2.vampirism and unit_2.health < health_limit:
                    unit_2.health += damage / 100 * unit_2.vampirism
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
        while (fighter_1.is_alive or army_1.army) and (
                fighter_2.is_alive or army_2.army
        ):
            if not fighter_1.is_alive:
                fighter_1 = army_1.army.pop(0)
            if not fighter_2.is_alive:
                fighter_2 = army_2.army.pop(0)
            fight(fighter_1, fighter_2, army_1, army_2)
        return bool(army_1.army or fighter_1.is_alive)


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

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
