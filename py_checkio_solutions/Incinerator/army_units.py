#!/usr/bin/env checkio --domain=py run army-units
class Army:
    def __init__(self):
        self.army_type = None
        self.army = {'swordsman': 'swordsman', 'lancer': 'lancer', 'archer': 'archer'}

    def train_swordsman(self, name):
        return Swordsman(name, self.army_type, self.army['swordsman'])

    def train_lancer(self, name):
        return Lancer(name, self.army_type, self.army['lancer'])

    def train_archer(self, name):
        return Archer(name, self.army_type, self.army['archer'])


class Swordsman:
    def __init__(self, name, army_type, role):
        self.name = name
        self.role = role
        self.army_type = army_type

    def introduce(self):
        return f'{self.role} {self.name}, {self.army_type} swordsman'


class Lancer:
    def __init__(self, name, army_type, role):
        self.name = name
        self.role = role
        self.army_type = army_type

    def introduce(self):
        return f'{self.role} {self.name}, {self.army_type} lancer'


class Archer:
    def __init__(self, name, army_type, role):
        self.name = name
        self.role = role
        self.army_type = army_type

    def introduce(self):
        return f'{self.role} {self.name}, {self.army_type} archer'


class AsianArmy(Army):
    def __init__(self):
        super(AsianArmy, self).__init__()
        self.army_type = 'Asian'
        self.army = {'swordsman': 'Samurai', 'lancer': 'Ronin', 'archer': 'Shinobi'}


class EuropeanArmy(Army):
    def __init__(self):
        super(EuropeanArmy, self).__init__()
        self.army_type = 'European'
        self.army = {'swordsman': 'Knight', 'lancer': 'Raubritter', 'archer': 'Ranger'}


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")


    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
