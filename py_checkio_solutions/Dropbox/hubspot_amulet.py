#!/usr/bin/env checkio --domain=py run hubspot-amulet
from itertools import product


def checkio(matrix):

    for lever_3, lever_2, lever_1 in product(range(181, -180, -1), range(181, -180, -1), range(181, -180, -1)):
        if (matrix[0][0] * lever_1 + matrix[1][0] * lever_2 + matrix[2][0] * lever_3) % 360 == 0 and (
            matrix[0][1] * lever_1 + matrix[1][1] * lever_2 + matrix[2][1] * lever_3) % 360 == 225 and (
            matrix[0][2] * lever_1 + matrix[1][2] * lever_2 + matrix[2][2] * lever_3) % 360 == 315:
            return [lever_1, lever_2, lever_3]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False


    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
