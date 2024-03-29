#!/usr/bin/env checkio --domain=py run monkey-typing
from functools import reduce


def count_words(text: str, words: set) -> int:
    return reduce(lambda x, y: x + 1 if y in text.lower() else x + 0, words, 0)


if __name__ == "__main__":
    print("Example:")
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
    ), "Example"
    assert (
            count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
    ), "BANANAS!"
    assert (
            count_words(
                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                {"sum", "hamlet", "infinity", "anything"},
            )
            == 1
    ), "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
