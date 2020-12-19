import math
import operator
from functools import reduce

import utils

input = utils.getInput(13).splitlines()

start = int(input[0])


class Bus:
    def __init__(self, id, position) -> None:
        super().__init__()
        self.id = int(id)
        self.position = int(position)
        self.last = None

    def __str__(self) -> str:
        return f"{self.id}"

    def next(self, after: int):
        return self.id * math.ceil(after / self.id)


busses = [Bus(i, p) for p, i in enumerate(input[1].split(","), start=0) if i != "x"]

min = None
currentBestBus = None

for bus in busses:
    ts = bus.next(start)
    if min is None or ts < min:
        min = ts
        currentBestBus = bus

print(f"part 1: {currentBestBus.id * (min - start)}")

invm = lambda a, b: 0 if a == 0 else 1 if b % a == 0 else b - invm(b % a, a) * b // a

N = reduce(operator.mul, [b.id for b in busses], 1)
x = sum([b.position * (N // b.id) * invm(N // b.id, b.id) for b in busses])

print(f"part 2: {N - x % N}")
