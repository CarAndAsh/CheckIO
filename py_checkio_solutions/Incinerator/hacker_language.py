#!/usr/bin/env checkio --domain=py run hacker-language
class HackerLanguage:
    def __init__(self):
        self.encode_msg = ''

    def write(self, text: str):
        self.encode_msg += ''.join(map(lambda symb: (bin(ord(symb))[2:] if symb.isalpha() else bin(ord(symb))[2:] + '0') if symb.isalpha() or symb == ' ' else symb,text))

    def delete(self, r_index: int):
        for _ in range(r_index):
            if set(self.encode_msg[-7:]) == {'1', '0'}:
                self.encode_msg = self.encode_msg[:-7]
            else:
                self.encode_msg = self.encode_msg[:-1]

    def send(self) -> str:
        return self.encode_msg

    def read(self, encoded_text) -> str:
        decoded_text = ''
        while encoded_text:
            encoded_part = encoded_text[:7]
            encoded_text = encoded_text[7:]
            if set(encoded_part) == {'1', '0'}:
                decoded_text += chr(int('0b' + ('100000' if encoded_part == '1000000' else encoded_part), 2))
            else:
                decoded_text += encoded_part[0]
                encoded_text = encoded_part[1:] + encoded_text

        return decoded_text


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
