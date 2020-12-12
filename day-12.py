import utils

input = utils.getInput(12)

commands = [(r[0], int(r[1:])) for r in input.splitlines()]


class logo:
    dir = None
    x = 0
    y = 0

    def __init__(self, dir="E") -> None:
        super().__init__()
        self.dir = dir

    def __str__(self) -> str:
        return f"{self.dir}: {self.x} {self.y}"

    def manhattanDistance(self):
        return abs(self.x) + abs(self.y)

    def processCommands(self, commands):
        print(self)
        for command in commands:
            self.process(command)
            print(f"{command}: {self}")

    def process(self, command):
        action, amount = command

        if action == "N":
            self.y += amount
        if action == "S":
            self.y -= amount
        if action == "E":
            self.x += amount
        if action == "W":
            self.x -= amount

        if action == "F":
            self.process((self.dir, amount))

        dirs = ["N", "E", "S", "W"]
        if action == "L":
            cur = dirs.index(self.dir) - (amount // 90)
            self.dir = dirs[cur % len(dirs)]
        if action == "R":
            cur = dirs.index(self.dir) + (amount // 90)
            self.dir = dirs[cur % len(dirs)]


l = logo()
l.processCommands(commands)
print(f"part 1: {l.manhattanDistance()}")
