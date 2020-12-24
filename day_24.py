from collections import defaultdict

import utils

input = utils.getInput(24)


class Grid:
    WHITE = True
    BLACK = False
    START = WHITE

    moves = {
        "e": (1, -1, 0),
        "se": (0, -1, 1),
        "sw": (-1, 0, 1),
        "w": (-1, 1, 0),
        "nw": (0, 1, -1),
        "ne": (1, 0, -1),
    }

    def __init__(self) -> None:
        super().__init__()
        self.grid = self._newGrid()
        self.reset()

    def _newGrid(self):
        return defaultdict(lambda: self.START)

    def _copyGrid(self):
        new = self._newGrid()
        for t in self.grid:
            if self.grid[t] != self.START:
                new[t] = self.grid[t]

        return new

    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def step(self, move):
        xo, yo, zo = self.moves[move]
        self.x += xo
        self.y += yo
        self.z += zo

    @classmethod
    def move(cls, pos, move):
        xo, yo, zo = cls.moves[move]
        x, y, z = pos

        return (x + xo, y + yo, z + zo)

    def flip(self):
        self.grid[(self.x, self.y, self.z)] = not self.grid[(self.x, self.y, self.z)]

    def parse(self, input: str):
        for line in input.splitlines():
            move = ""
            for c in line:
                move += c
                if c != "n" and c != "s":
                    self.step(move)
                    move = ""
            self.flip()
            self.reset()

    def _getRanges(self):
        xs, ys, zs = [], [], []
        for key in self.grid:
            x, y, z = key
            xs.append(x)
            ys.append(y)
            zs.append(z)

        return (
            range(min(xs) - 1, max(xs) + 2),
            range(min(ys) - 1, max(ys) + 2),
            range(min(zs) - 1, max(zs) + 2),
        )

    def gameRound(self):
        newGrid = self._copyGrid()

        rx, ry, rz = self._getRanges()

        for x in rx:
            for y in ry:
                for z in rz:
                    key = (x, y, z)
                    adjBlack = 0
                    adjWhite = 0
                    for move in self.moves:
                        pos = self.move(key, move)
                        if self.grid[pos] == self.WHITE:
                            adjWhite += 1
                        else:
                            adjBlack += 1
                    if self.grid[key] == self.BLACK:
                        if adjBlack == 0 or adjBlack > 2:
                            newGrid[key] = self.WHITE
                    else:
                        if adjBlack == 2:
                            newGrid[key] = self.BLACK

        self.grid = newGrid

    @property
    def whiteCount(self):
        return sum([True for g in self.grid.values() if g == self.WHITE])

    @property
    def blackCount(self):
        return sum([True for g in self.grid.values() if g == self.BLACK])


grid = Grid()
grid.parse(input)
print(f"part 1: {grid.blackCount}")

for i in range(100):
    grid.gameRound()
    print(f"day {i}")

print(f"part 2: {grid.blackCount}")
