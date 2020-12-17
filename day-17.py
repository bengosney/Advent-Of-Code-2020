from collections import defaultdict

import utils

input = utils.getInput(17)

input = """
.#.
..#
###
""".strip()


def getNewSpace():
    return defaultdict(lambda: False)


workingSpace = getNewSpace()


def maxSpace():
    return range(-4, 8)


def draw(space):
    print("=" * 80)
    for z in maxSpace():
        screen = f"z: {z}\n"
        for x in maxSpace():
            row = []
            for y in maxSpace():
                if space[(x, y, z)]:
                    row.append("#")
                else:
                    row.append(".")
            screen += f"{''.join(row)}\n"

        if "#" in screen:
            print(screen)


def countAdj(space, x, y, z):
    true = 0
    c = 0
    for _x in (-1, 0, 1):
        for _y in (-1, 0, 1):
            for _z in (-1, 0, 1):
                if (_x, _y, _z) == (0, 0, 0):
                    continue

                if space[(x + _x, y + _y, z + _z)]:
                    true += 1
    return true


def cycle(space):
    new = getNewSpace()

    for x in maxSpace():
        for y in maxSpace():
            for z in maxSpace():
                if (x, y, z) == (0, 0, -1):
                    bob = 1
                adj = countAdj(space, x, y, z)
                if space[(x, y, z)] and (adj < 2 or adj > 3):
                    new[(x, y, z)] == False
                elif not space[(x, y, z)] and adj == 3:
                    new[(x, y, z)] == True
                elif space[(x, y, z)]:
                    new[(x, y, z)] = space[(x, y, z)]

    return new


for x, row in enumerate(input.splitlines()):
    for y, col in enumerate(row):
        if col == "#":
            workingSpace[(x, y, 0)] = True
        else:
            workingSpace[(x, y, 0)] = False

draw(workingSpace)
draw(cycle(workingSpace))

for i in range(6):
    print(f"cycle {i}")
    workingSpace = cycle(workingSpace)

print(f"part 1: {sum(workingSpace.items())}")
