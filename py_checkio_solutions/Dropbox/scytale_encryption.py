#!/usr/bin/env checkio --domain=py run scytale-encryption
from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    decipher_lst = []
    i = 1
    while len(decipher_lst) != len(ciphertext):
        decipher_word = ''.join([ciphertext[j::i] for j in range(i)])
        decipher_lst.append(decipher_word)
        i += 1
    res = list(filter(lambda phrase: crib in phrase, decipher_lst))
    return res[0] if len(res) == 1 else None


if __name__ == "__main__":
    print("Example:")
    print(scytale_decipher("hdoeerlallrdow", "world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (
            scytale_decipher("totetshpmeecisendysescwticsriasraytlaegphet", "sicret")
            == None
    ), "Crib is not in plaintext"
    assert (
            scytale_decipher("aaaatctwtkdn", "at") == None
    ), "More than one possible decryptions"
    assert scytale_decipher("atcadwtaktan", "attackatdawn") == "attackatdawn"
    assert scytale_decipher("mateneetaltnettvhithieenmeonegesniv", "eleven") == None
    assert scytale_decipher("tpsyhhsspsieatcscgeyiredtseewaatniltmcteoer",
                            "secret") == "thisisatopsecretmessageencryptedwithscytale"
    assert scytale_decipher("mtieanetttihmoeeneaevtletenhvieensng", "eve") == None
    assert scytale_decipher(
        "solnacaeyacndcpenessyeerhsckpftosyiuisaaaftpcsenrrltktdenataehnoedtmasieogvbgenbsowriyrlsc",
        "scytale") == "scytaleisoneoftheoldestknowncryptographicdevicesusedbyancientgreeksnamelyspartansasfarasbc"

    print("Coding complete? Click 'Check' to earn cool rewards!")
