from math import sqrt
from typing import Dict, List, Literal, Tuple

import utils

input = utils.getInput(20)

rawTiles = input.split("\n\n")

Row = List[str]
Sides = Literal["top", "right", "bottom", "left"]
AllSides = Tuple[Sides, Sides, Sides, Sides]


class Tile:
    def __init__(self, id: int, data: Dict[Tuple[int, int], str]) -> None:
        super().__init__()
        self.id: int = id
        self.data: Dict[Tuple[int, int], str] = data

    @classmethod
    def parse(cls, rawTitle: str) -> "Tile":
        id = 0
        lines = {}
        y = 0
        for line in rawTitle.splitlines():
            if "Tile" in line:
                id = int(line.split(" ")[1].strip(":"))
            else:
                for x, c in enumerate(line):
                    lines[(x, y)] = c
                y += 1

        return cls(id, lines)

    def __str__(self) -> str:
        line = ""
        for i, k in enumerate(self.data):
            line += self.data[k]
            if (i % self.size) + 1 == self.size:
                line += "\n"

        return line

    def row(self, r: int) -> Row:
        return [self.data[(x, r)] for x in range(self.size)]

    @property
    def size(self) -> int:
        return int(sqrt(len(self.data)))

    @property
    def top(self) -> Row:
        return self.row(0)

    @property
    def bottom(self) -> Row:
        return self.row(self.size - 1)

    @property
    def left(self) -> Row:
        return [self.data[(0, y)] for y in range(self.size)]

    @property
    def right(self) -> Row:
        return [self.data[(self.size - 1, y)] for y in range(self.size)]

    def flipX(self) -> None:
        new = {}
        for y in range(self.size):
            for x in range(self.size):
                nx = (self.size - x) - 1
                new[(nx, y)] = self.data[(x, y)]
        self.data = new

    def flipY(self) -> None:
        new = {}
        for y in range(self.size):
            ny = (self.size - y) - 1
            for x in range(self.size):
                new[(x, ny)] = self.data[(x, y)]
        self.data = new

    def rotate(self) -> None:
        new = {}
        for y in range(self.size):
            ny = (self.size - y) - 1
            for x in range(self.size):
                new[(ny, x)] = self.data[(x, y)]
        self.data = new

    def draw(self) -> None:
        for y in range(self.size):
            for x in range(self.size):
                print(self.data[(x, y)], end="")
            print()

    def fits(self, tile: "Tile") -> List[Tuple[Sides, Sides, bool]]:
        sides: AllSides = ("top", "right", "bottom", "left")
        fits = []
        for selfSide in sides:
            side1 = "".join(getattr(self, selfSide))
            for otherSide in sides:
                side2 = "".join(getattr(tile, otherSide))
                if side1 == side2:
                    fits.append((selfSide, otherSide, False))
                if side1 == side2[::-1]:
                    fits.append((selfSide, otherSide, True))

        return fits

    def removeBorder(self) -> None:
        new = {}
        for y in range(1, self.size - 1):
            for x in range(1, self.size - 1):
                new[(x - 1, y - 1)] = self.data[(x, y)]

        self.data = new


Grid = Dict[Tuple[int, int], Tile]


def minGrid(grid: Grid) -> Tuple[int, int]:
    return min(k[0] for k in grid), min(k[1] for k in grid)


def maxGrid(grid: Grid) -> Tuple[int, int]:
    return max(k[0] for k in grid), max(k[1] for k in grid)


tiles = []
for rawTile in rawTiles:
    tile = Tile.parse(rawTile)
    tiles.append(tile)


def part1() -> int:
    ids = []
    for t1 in tiles:
        fits = []
        for t2 in tiles:
            if t1.id != t2.id:
                fits += t1.fits(t2)
        if len(fits) == 2:
            ids.append(t1.id)

    part1 = 1
    for id in ids:
        part1 *= id

    return part1


print(f"part 1: {part1()}")

validMatches = [
    ("left", "right", False),
    ("right", "left", False),
    ("top", "bottom", False),
    ("bottom", "top", False),
]

placedIDs: List[int] = []
grid: Grid = {}
while len(placedIDs) < len(tiles):
    for tile in tiles:
        if tile.id in placedIDs:
            continue

        if len(grid) == 0:
            grid[(0, 0)] = tile
            placedIDs.append(tile.id)
            continue

        for x, y in grid:
            fits = grid[(x, y)].fits(tile)
            if len(fits) > 0:
                correctFit = None
                placedIDs.append(tile.id)
                i = 0
                while correctFit is None:
                    fit = grid[(x, y)].fits(tile)[0]
                    if fit not in validMatches:
                        tile.rotate()
                    else:
                        correctFit = fit
                        break

                    i += 1
                    if i in {4, 12}:
                        tile.flipX()
                    elif i == 8:
                        tile.flipY()
                if correctFit[0] == "top":
                    grid[(x, y + 1)] = tile
                if correctFit[0] == "right":
                    grid[(x + 1, y)] = tile
                if correctFit[0] == "bottom":
                    grid[(x, y - 1)] = tile
                if correctFit[0] == "left":
                    grid[(x - 1, y)] = tile
                break

minX, minY = minGrid(grid)
maxX, maxY = maxGrid(grid)

data = {}
ax = abs(minX)
ay = abs(minY)
gx, gy = 0, 0
bpb = 1
for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
        grid[(x, y)].removeBorder()
        mx = (ax + x) * grid[(x, y)].size
        my = (ay + y) * grid[(x, y)].size
        for cy in range(grid[(x, y)].size):
            for cx in range(grid[(x, y)].size):
                px = mx + cx
                py = my + cy

                data[(px, py)] = grid[(x, y)].data[(cx, cy)]


monster = """
                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""


bigTile = Tile(0, data)

for i in range(24):
    line = f"{bigTile}".replace("\n", "")
    if "#    ##    ##    ###".replace(" ", ".") in line:
        break

    bigTile.rotate()
    if i in [4, 12]:
        bigTile.flipX()
    elif i == 8:
        bigTile.flipY()
mCount = 0
line = f"{bigTile}".replace("\n", "")
mods = [0, 5, 6, 11, 12, 17, 18, 19]
for i, _ in enumerate(line):
    res = []
    try:
        for m in mods:
            res.append(line[i + m] == "#")
    except IndexError:
        break

    if all(res):
        mCount += 1

num = f"{bigTile}".count("#")
numInM = monster.count("#")
print(f"part 2: {num - (mCount * numInM)}")
