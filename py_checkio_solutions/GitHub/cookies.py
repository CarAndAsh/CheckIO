#!/usr/bin/env checkio --domain=py run cookies
def get_cookie(cookie, name):
    return {pair.split('=')[0]: pair.split('=', 1)[1] for pair in cookie.split("; ")}[name]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            get_cookie("_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true", "ffo") == "true"
    ), "ffo=true"
    assert (
            get_cookie("theme=light; sessionToken=abc123", "theme") == "light"
    ), "theme=light"
    print("Looks like you know everything. It is time for 'Check'!")
