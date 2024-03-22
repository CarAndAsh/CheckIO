#!/usr/bin/env checkio --domain=py run dialogues
VOWELS = "aeiou"


class Chat:
    def __init__(self):
        # chat = {(by,to):[]}}
        self.dialogue_dict = {}
        self.companion_by = None
        self.companion_to = None

    def create_continue_chat(self):
        return self.dialogue_dict.setdefault((self.companion_by.name, self.companion_to.name), [])

    def connect_human(self, human):
        self.companion_by = human
        if self.companion_to:
            self.companion_to.chat = self.create_continue_chat()
            self.companion_by.chat = self.create_continue_chat()

    def connect_robot(self, robot):
        self.companion_to = robot
        if self.companion_by:
            self.companion_to.chat = self.create_continue_chat()
            self.companion_by.chat = self.create_continue_chat()

    def show_human_dialogue(self):
        return '\n'.join(title+msg for title, msg in (self.dialogue_dict[(self.companion_by.name, self.companion_to.name)]))

    def show_robot_dialogue(self):
        return '\n'.join((title + ''.join(map(lambda ch: '0' if ch.lower() in VOWELS else '1', msg)) for title, msg in self.dialogue_dict[(self.companion_by.name, self.companion_to.name)]))


class Human:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, msg):
        self.chat.append((f'{self.name} said: ', msg))


class Robot:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, msg):
        self.chat.append((f'{self.name} said: ', msg))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert (
            chat.show_human_dialogue()
            == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    )
    assert (
            chat.show_robot_dialogue()
            == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
    )

    print("Coding complete? Let's try tests!")
