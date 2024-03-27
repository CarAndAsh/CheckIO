#!/usr/bin/env checkio --domain=py run party-invitations
class Friend:
    def __init__(self, name: str):
        self.name = name
        self.invites = []

    def show_invite(self) -> str:
        return self.invites[-1] if self.invites else "No party..."


class Party:
    def __init__(self, event: str):
        self.event = event
        self.friends = set()

    def add_friend(self, friend: Friend):
        self.friends.add(friend)

    def send_invites(self, invite: str):
        [friend.invites.append(self.event+': '+invite) for friend in self.friends]

    def del_friend(self, friend: Friend):
        self.friends.remove(friend)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
