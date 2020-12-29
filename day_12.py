import math
from abc import ABC, abstractmethod
from typing import List, Literal, Tuple

import utils

input = utils.getInput(12)
commands = [(r[0], int(r[1:])) for r in input.splitlines()]

Dirs = Literal["N", "E", "S", "W"]
Command = Tuple[Dirs, int]


class Base(ABC):
    x: int = 0
    y: int = 0

    def __init__(self, dir: Dirs = "E", x=0, y=0) -> None:
        super().__init__()
        self.dir: Dirs = dir
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"{self.manhattanDistance()}"

    def manhattanDistance(self):
        return abs(self.x) + abs(self.y)

    def processCommands(self, commands):
        for command in commands:
            self.process(command)

    @abstractmethod
    def process(self, command):
        pass


class Ship(Base):
    def process(self, command: Command):
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

        dirs: List[Dirs] = ["N", "E", "S", "W"]
        if action == "L":
            cur = dirs.index(self.dir) - (amount // 90)
            self.dir = dirs[cur % len(dirs)]
        if action == "R":
            cur = dirs.index(self.dir) + (amount // 90)
            self.dir = dirs[cur % len(dirs)]


class Waypoint(Base):
    e = 0
    n = 0

    def manhattanDistance(self):
        return abs(self.e) + abs(self.n)

    def rotate(self, angle):
        a = math.radians(angle)

        x = math.cos(a) * self.x - math.sin(a) * self.y
        y = math.sin(a) * self.x + math.cos(a) * self.y

        return round(x), round(y)

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


ship = Ship()
ship.processCommands(commands)
print(f"part 1: {ship.manhattanDistance()}")

waypoint = Waypoint(x=10, y=1)
waypoint.processCommands(commands)
print(f"part 2: {waypoint.manhattanDistance()}")
