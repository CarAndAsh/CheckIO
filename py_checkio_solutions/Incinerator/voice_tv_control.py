#!/usr/bin/env checkio --domain=py run voice-tv-control
from typing import Iterable


class VoiceCommand:
    def __init__(self, collection: Iterable):
        self.__collection = collection
        self.__col_len = len(self.__collection)
        self.__current = 0

    def first_channel(self) -> str:
        self.__current = 0
        return self.__collection[0]

    def last_channel(self) -> str:
        self.__current = self.__col_len - 1
        return self.__collection[-1]

    def turn_channel(self, ind: int) -> str:
        self.__current = (ind - 1) % self.__col_len
        return self.__collection[self.__current]

    def next_channel(self) -> str:
        self.__current = (self.__current + 1) % self.__col_len
        return self.__collection[self.__current]

    def previous_channel(self) -> str:
        self.__current = (self.__current - 1) % self.__col_len
        return self.__collection[self.__current]

    def current_channel(self) -> str:
        return self.__collection[self.__current % self.__col_len]

    def is_exist(self, ind_or_name: int | str) -> str:
        if isinstance(ind_or_name, int):
            return 'Yes' if 0 < ind_or_name < self.__col_len else 'No'
        if isinstance(ind_or_name, str):
            return 'Yes' if ind_or_name in self.__collection else 'No'


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
