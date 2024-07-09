#!/usr/bin/env checkio --domain=py run halloween-monsters
from collections import Counter
from copy import deepcopy

MONSTERS = """
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
"""


def halloween_monsters(spell: str | dict) -> int:
    monsters_dicts = (Counter(m) for m in MONSTERS.split('\n')[1:-1])
    monsters_in_spell = []
    spell_dict = Counter(spell)
    for monster_dict in monsters_dicts:
        if all(map(lambda ch: monster_dict[ch] <= spell_dict[ch], monster_dict)):
            monsters_in_spell.append(monster_dict)

    def max_names(spell_dict):
        c_list = [0]
        for monster in monsters_in_spell:
            if all(map(lambda ch: monster[ch] <= spell_dict[ch], monster)):
                spell_dict_dc = deepcopy(spell_dict)
                for ch in monster:
                    spell_dict_dc[ch] -= monster[ch]
                c_list.append(1 + max_names(spell_dict_dc))
        return max(c_list)

    return max_names(spell_dict)


if __name__ == "__main__":
    assert halloween_monsters("casjokthg") == 2, "jack ghost"
    assert halloween_monsters("leumooeeyzwwmmirbmf") == 3, "mummy zombie werewolf"
    assert halloween_monsters("nafrweiicttwneshhtikcn") == 3, "witch witch frankenstein"
    assert halloween_monsters("kenoistcepajmlvre") == 2, "skeleton vampire (not jack)"
    assert halloween_monsters("miaimavrurymepepv") == 2, "vampire vampire (not mummy)"
    assert halloween_monsters(
        "jqfbjivldrcuuapmnvjuhwgozsfsnwualqbnsxrrbvwfzxnpmekafwxhgkxtebtyclqhqmitzhgzkmcyecdpoyddetokip") == 9
    print("Your spell seem to be okay. It's time to check.")
