import re
from collections import defaultdict

import utils

input = utils.getInput(24)

input = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

regex = r"(e|se|sw|w|nw|ne)"

WHITE = True
BLACK = False

moves = {
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
}


class Grid:
    def __init__(self) -> None:
        super().__init__()
        self.grid = defaultdict(lambda: WHITE)
        self.x = 0
        self.y = 0
        self.z = 0

    def step(self, move):
        xo, yo, zo = moves[move]
        self.x += xo
        self.y += yo
        self.z += zo

        self.grid[(self.x, self.y, self.z)] = not self.grid[(self.x, self.y, self.z)]

    def parse(self, input: str):
        for line in input.splitlines():
            matches = re.finditer(regex, line, re.MULTILINE)
            for match in matches:
                for group in match.groups():
                    self.step(group)

    @property
    def whiteCount(self):
        return sum([True for g in self.grid.values() if g == WHITE])

    @property
    def blackCount(self):
        return sum([True for g in self.grid.values() if g == BLACK])


grid = Grid()
grid.parse(input)
print(grid.blackCount)
