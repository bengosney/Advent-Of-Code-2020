from collections import defaultdict

import utils

input = utils.getInput(24)

inputy = """sesenwnenenewseeswwswswwnenewsewsw
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
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def step(self, move):
        xo, yo, zo = moves[move]
        self.x += xo
        self.y += yo
        self.z += zo

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

    @property
    def whiteCount(self):
        return sum([True for g in self.grid.values() if g == WHITE])

    @property
    def blackCount(self):
        return sum([True for g in self.grid.values() if g == BLACK])


grid = Grid()
grid.parse(input)
print(f"part 1: {grid.blackCount}")
