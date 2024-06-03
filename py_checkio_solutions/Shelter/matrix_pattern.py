#!/usr/bin/env checkio --domain=py run matrix-pattern
def checkio(pattern, image):
    for i in range(len(image) - len(pattern) + 1):
        for j in range(len(image[0]) - len(pattern[0]) + 1):
            if all((image[i + di][j + dj] == pattern[0 + di][0 + dj] for dj in range(len(pattern[0])) for di in range(len(pattern)))):
                for di in range(len(pattern)):
                    for dj in range(len(pattern[0])):
                        image[i + di][j + dj] += 2
    return image


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
