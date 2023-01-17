from collections import defaultdict

import utils

input = utils.getInput(17)


workingSpace = defaultdict(lambda: False)
workingSpace4 = defaultdict(lambda: False)


def getMaxSpace(space):
    x = set([0])
    y = set([0])
    z = set([0])
    for i in space:
        if space[i]:
            x.add(i[0])
            y.add(i[1])
            z.add(i[2])

    return (
        range(min(x) - 1, max(x) + 2),
        range(min(y) - 1, max(y) + 2),
        range(min(z) - 1, max(z) + 2),
    )


def getMaxSpace4(space):
    x = set([0])
    y = set([0])
    z = set([0])
    w = set([0])
    for i in space:
        if space[i]:
            x.add(i[0])
            y.add(i[1])
            z.add(i[2])
            w.add(i[2])

    return (
        range(min(x) - 1, max(x) + 2),
        range(min(y) - 1, max(y) + 2),
        range(min(z) - 1, max(z) + 2),
        range(min(w) - 1, max(w) + 2),
    )


def countAdj(space, x, y, z):
    true = 0
    for _x in (-1, 0, 1):
        for _y in (-1, 0, 1):
            for _z in (-1, 0, 1):
                if (_x, _y, _z) == (0, 0, 0):
                    continue

                if space[(x + _x, y + _y, z + _z)]:
                    true += 1

    return true


def countAdj4(space, x, y, z, w):
    true = 0
    for _x in (-1, 0, 1):
        for _y in (-1, 0, 1):
            for _z in (-1, 0, 1):
                for _w in (-1, 0, 1):
                    if (_x, _y, _z, _w) == (0, 0, 0, 0):
                        continue

                    if space[(x + _x, y + _y, z + _z, w + _w)]:
                        true += 1

    return true


def cycle(space):
    new = defaultdict(lambda: False)
    rx, ry, rz = getMaxSpace(space)
    for x in rx:
        for y in ry:
            for z in rz:
                adj = countAdj(space, x, y, z)
                if adj < 2 or adj > 3:
                    pass
                elif adj == 3 or space[(x, y, z)]:
                    new[(x, y, z)] = True

    return new


def cycle4(space):
    new = defaultdict(lambda: False)
    rx, ry, rz, rw = getMaxSpace4(space)
    for x in rx:
        for y in ry:
            for z in rz:
                for w in rw:
                    adj = countAdj4(space, x, y, z, w)
                    if adj < 2 or adj > 3:
                        pass
                    elif adj == 3 or space[(x, y, z, w)]:
                        new[(x, y, z, w)] = True

    return new


for x, row in enumerate(input.splitlines()):
    for y, col in enumerate(row):
        if col == "#":
            workingSpace[(x, y, 0)] = True
            workingSpace4[(x, y, 0, 0)] = True

for _ in range(6):
    workingSpace = cycle(workingSpace)
    workingSpace4 = cycle4(workingSpace4)

print(f'part 1: {sum(True for i in workingSpace if workingSpace[i])}')
print(f'part 2: {sum(True for i in workingSpace4 if workingSpace4[i])}')
