from math import sqrt

import utils

input = utils.getInput(20)

input1 = """Tile 1:
1234
5678
9abc
defg"""

rawTiles = input.split("\n\n")


class Tile:
    def __init__(self, id: int, data: list()) -> None:
        super().__init__()
        self.id = id
        self.data = data

    @classmethod
    def parse(cls, rawTitle: str) -> "Tile":
        id = None
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

    @property
    def size(self):
        return int(sqrt(len(self.data)))

    @property
    def top(self):
        return [self.data[(x, 0)] for x in range(self.size)]

    @property
    def bottom(self):
        return [self.data[(x, self.size - 1)] for x in range(self.size)]

    @property
    def left(self):
        return [self.data[(0, y)] for y in range(self.size)]

    @property
    def right(self):
        return [self.data[(self.size - 1, y)] for y in range(self.size)]

    def flipX(self):
        new = {}
        for y in range(self.size):
            for x in range(self.size):
                nx = (self.size - x) - 1
                new[(nx, y)] = self.data[(x, y)]
        self.data = new

    def flipY(self):
        new = {}
        for y in range(self.size):
            for x in range(self.size):
                ny = (self.size - y) - 1
                new[(x, ny)] = self.data[(x, y)]
        self.data = new

    def rotate(self):
        new = {}
        for y in range(self.size):
            for x in range(self.size):
                ny = (self.size - y) - 1
                new[(ny, x)] = self.data[(x, y)]
        self.data = new

    def draw(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.data[(x, y)], end="")
            print()

    def fits(self, tile):
        sides = ("top", "right", "bottom", "left")
        fits = []
        for selfSide in sides:
            for otherSide in sides:
                side1 = "".join(getattr(self, selfSide))
                side2 = "".join(getattr(tile, otherSide))
                if side1 == side2:
                    fits.append((selfSide, otherSide, False))
                if side1 == side2[::-1]:
                    fits.append((selfSide, otherSide, True))

        return fits


class Grid:
    def __init__(self) -> None:
        super().__init__()
        self.grid = {}

    def __len__(self) -> int:
        return len(self.grid)

    def min(self):
        return min([k[0] for k in self.grid]), min([k[0] for k in self.grid])

    def max(self):
        return max([k[0] for k in self.grid]), max([k[0] for k in self.grid])


tiles = []
for rawTile in rawTiles:
    tile = Tile.parse(rawTile)
    tiles.append(tile)

tiles[0].draw()
print()
tiles[1].draw()

ids = []
for t1 in tiles:
    fits = []
    for t2 in tiles:
        if t1.id != t2.id:
            fits += t1.fits(t2)
    if len(fits) == 2:
        ids.append(t1.id)
    else:
        bob = 1

part1 = 1
for id in ids:
    part1 *= id
print(f"part 1: {part1}")
exit(0)

grid = {}
current = None
for tile in tiles:
    if len(grid) == 0:
        grid[(0, 0)] = tile
        current = tile
        continue

    for x, y in grid:
        fits = grid[(x, y)].fits(tile)
        if len(fits) > 0:
            pass
