#!/usr/bin/env checkio --domain=py run remove-accents
import unicodedata


def checkio(input_str):
        return ''.join(char for char in unicodedata.normalize('NFD', input_str)
                       if unicodedata.category(char) != 'Mn')

# These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    print(checkio(u"loài trăn lớn"))
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    assert checkio("àèìǹòùẁỳÀÈÌǸÒÙẀỲ") == "aeinouwyAEINOUWY"
    print('Done')
