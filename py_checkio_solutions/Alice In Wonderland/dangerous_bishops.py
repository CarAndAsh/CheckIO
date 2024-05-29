#!/usr/bin/env checkio --domain=py run dangerous-bishops
def safe_squares(n: int, bishops: tuple[int, int]) -> int:
    danger_cells = set(bishops) if bishops else set()

    def covered_cells(n, bishop, step=1):
        cell_1, cell_2 = list(bishop), list(bishop)
        while -1 not in cell_1 and n not in cell_1:
            danger_cells.add(tuple(cell_1))
            cell_1[1] += step
            cell_1[0] -= step
        while -1 not in cell_2 and n not in cell_2:
            danger_cells.add(tuple(cell_2))
            cell_2[1] += step
            cell_2[0] += step

    for bishop in bishops:
        covered_cells(n, bishop)
        covered_cells(n, bishop, -1)
    return n ** 2 - len(danger_cells) if danger_cells else n ** 2


print("Example:")
print(safe_squares(10, []))

# These "asserts" are used for self-checking
assert safe_squares(10, []) == 100
assert safe_squares(4, [(2, 3), (0, 1)]) == 11
assert safe_squares(8, [(1, 1), (3, 5), (7, 0), (7, 6)]) == 29

print("The mission is done! Click 'Check Solution' to earn rewards!")
