#!/usr/bin/env checkio --domain=py run the-hollow-diamond
from string import ascii_lowercase


def hollow_diamond(side: int, length: int, cw: bool) -> str:
    chars = ascii_lowercase[:length]
    num_fig_symb = 4 * (side - 1)
    res = []
    if length < num_fig_symb:
        chars += '*' * (num_fig_symb - length)
    for i in range(num_fig_symb // 2 + 1):
        interval = abs(side - (i + 1))
        line = ' ' * interval
        if i == 0 or i == 2 * side - 2:
            line += chars[i]
        elif cw:
            line += chars[-i] + ' ' * (abs(side - interval - 1) * 2 - 1) + chars[i]
        else:
            line += chars[i] + ' ' * (abs(side - interval - 1) * 2 - 1) + chars[-i]
        res.append(line)
    return '\n'.join(res)


print("Example:")
print(hollow_diamond(4, 10, False))

# These "asserts" are used for self-checking
assert (hollow_diamond(3, 8, True) == "  a\n"
                                      " h b\n"
                                      "g   c\n"
                                      " f d\n"
                                      "  e")
assert (hollow_diamond(3, 6, False) == "  a\n"
                                       " b *\n"
                                       "c   *\n"
                                       " d f\n"
                                       "  e")
assert (hollow_diamond(4, 10, False) == "   a\n"
                                        "  b *\n"
                                        " c   *\n"
                                        "d     j\n"
                                        " e   i\n"
                                        "  f h\n"
                                        "   g"
        )
assert (hollow_diamond(5, 16, True) == "    a\n"
                                       "   p b\n"
                                       "  o   c\n"
                                       " n     d\n"
                                       "m       e\n"
                                       " l     f\n"
                                       "  k   g\n"
                                       "   j h\n"
                                       "    i"
        )
assert (hollow_diamond(5, 14, False) == "    a\n"
                                        "   b *\n"
                                        "  c   *\n"
                                        " d     n\n"
                                        "e       m\n"
                                        " f     l\n"
                                        "  g   k\n"
                                        "   h j\n"
                                        "    i"
        )

print("The mission is done! Click 'Check Solution' to earn rewards!")
