import math

import utils

inputBlocks = utils.getInput(16).split("\n\n")

inputBlocksy = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split(
    "\n\n"
)


class Rule:
    def __init__(self, name: str, ranges: list) -> None:
        super().__init__()
        self.name = name
        self.ranges = ranges

    def __str__(self) -> str:
        return f"{self.name}: {self.ranges}"

    @classmethod
    def parse(cls, row):
        name, ranges = [s.strip() for s in row.split(":")]

        parsedRanges = []
        for range in [s.strip() for s in ranges.split("or")]:
            parsedRanges.append([int(r) for r in range.split("-")])

        return cls(name, parsedRanges)


class Ticket:
    def __init__(self, numbers: list) -> None:
        super().__init__()
        self.numbers = numbers

    @classmethod
    def parse(cls, row):
        return cls([int(i) for i in row.split(",")])

    def check(self, rules) -> int:
        err = 0
        for i in self.numbers:
            failed = []
            for rule in rules:

                for r in rule.ranges:
                    if i < r[0] or i > r[1]:
                        failed.append(True)
                    else:
                        failed.append(False)
            if all(failed):
                err += i
        return err

    def setinvalidMap(self, rules, invalidMap):
        for col, i in enumerate(self.numbers):
            for rule in rules:
                ruleFailed = []
                for r in rule.ranges:
                    if i < r[0] or i > r[1]:
                        ruleFailed.append(True)
                    else:
                        ruleFailed.append(False)

                if all(ruleFailed):
                    invalidMap[rule.name].add(col)


rules = []
for row in inputBlocks[0].splitlines():
    rules.append(Rule.parse(row))

tickets = []
for row in inputBlocks[2].splitlines():
    if "ticket" in row:
        continue

    tickets.append(Ticket.parse(row))

myTicket = Ticket.parse(inputBlocks[1].splitlines()[1])

errorRate = 0
validTickets = []
for ticket in tickets:
    err = ticket.check(rules)
    if err == 0:
        validTickets.append(ticket)
    errorRate += err

print(f"part 1: {errorRate}")

invalidMap = {r.name: set() for r in rules}

for ticket in validTickets:
    ticket.setinvalidMap(rules, invalidMap)


cols = list(range(len(tickets[0].numbers)))
names = [r.name for r in rules]
colmap = {}
while len(names) > 1:
    for key in invalidMap:
        if len(invalidMap[key]) == len(names) - 1:
            validCols = [c for c in cols if c not in invalidMap[key]]
            colmap[key] = validCols[0]
            cols.remove(validCols[0])
            names.remove(key)

fullMap = {}
departures = []
for col in colmap:
    fullMap[col] = myTicket.numbers[colmap[col]]
    if "departure" in col:
        departures.append(myTicket.numbers[colmap[col]])

print(f"part 2: {math.prod(departures)}")
