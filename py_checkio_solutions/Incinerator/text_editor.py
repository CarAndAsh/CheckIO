#!/usr/bin/env checkio --domain=py run text-editor
class Text:

    def write(self, text: str):
        if 'text' in self.__dict__:
            self.text += text
        else:
            self.text = text

    def set_font(self, font: str):
        self.font = font

    def show(self):
        return f'{("[" + self.font + "]") if "font" in self.__dict__ else ""}{self.text or ""}{("[" + self.font + "]") if "font" in self.__dict__ else ""}'

    def restore(self, snapshot):
        attr_tpl = tuple(self.__dict__.keys())
        for attr in attr_tpl:
            if attr in snapshot:
                self.__setattr__(attr, snapshot[attr])
            else:
                delattr(self, attr)


class SavedText:
    def __init__(self):
        self.state_lst = []

    def save_text(self, cls_text: Text):
        self.state_lst.append({atr: cls_text.__getattribute__(atr) for atr in cls_text.__dict__})

    def get_version(self, version: int):
        return self.state_lst[version]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "
    
    print("Coding complete? Let's try tests!")
