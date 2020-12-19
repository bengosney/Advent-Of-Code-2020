import math

import utils

input = utils.getInput(12)
commands = [(r[0], int(r[1:])) for r in input.splitlines()]


class base:
    dir = None
    x = 0
    y = 0

    def __init__(self, dir="E", x=0, y=0) -> None:
        super().__init__()
        self.dir = dir
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"{self.manhattanDistance()}"

    def manhattanDistance(self):
        return abs(self.x) + abs(self.y)

    def processCommands(self, commands):
        for command in commands:
            self.process(command)


class ship(base):
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


class waypoint(base):
    e = 0
    n = 0

    def manhattanDistance(self):
        return abs(self.e) + abs(self.n)

    def rotate(self, angle):
        a = math.radians(angle)

        x = math.cos(a) * self.x - math.sin(a) * self.y
        y = math.sin(a) * self.x + math.cos(a) * self.y
        self.x, self.y = round(x), round(y)

    def __str__(self) -> str:
        return f"{self.dir}: {self.x} {self.y} || {self.e} {self.n} || {self.x - self.e} {self.y - self.n}"

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
            self.e += self.x * amount
            self.n += self.y * amount

        if action == "L":
            self.x, self.y = self.rotate(amount)
        if action == "R":
            self.x, self.y = self.rotate(-amount)


ship = ship()
ship.processCommands(commands)
print(f"part 1: {ship.manhattanDistance()}")

waypoint = waypoint(x=10, y=1)
waypoint.processCommands(commands)
print(f"part 2: {waypoint.manhattanDistance()}")
