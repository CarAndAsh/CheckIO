#!/usr/bin/env checkio --domain=py run friends
class Friends:
    def __init__(self, connections):
        self.connections = dict()
        for user_1, user_2 in connections:
            self.connections.setdefault(user_1, set()).add(user_2)
            self.connections.setdefault(user_2, set()).add(user_1)

    def add(self, connection) -> bool:
        user_1, user_2 = connection
        if user_2 in self.connections.get(user_1, set()) or user_1 in self.connections.get(user_2, set()):
            return False
        self.connections.setdefault(user_1, set()).add(user_2)
        self.connections.setdefault(user_2, set()).add(user_1)
        return True

    def remove(self, connection) -> bool:
        user_1, user_2 = connection
        if user_1 in self.connections.get(user_2, set()) and user_2 in self.connections.get(user_1, set()):
            self.connections[user_1].discard(user_2)
            if not self.connections[user_1]:
                del self.connections[user_1]
            self.connections[user_2].discard(user_1)
            if not self.connections[user_2]:
                del self.connections[user_2]
            return True
        return False

    def names(self) -> set:
        return set(self.connections.keys())

    def connected(self, name) -> set:
        return self.connections.get(name, set())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
