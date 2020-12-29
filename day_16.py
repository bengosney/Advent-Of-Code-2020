from typing import Dict, List, Set

import utils

inputBlocks = utils.getInput(16).split("\n\n")


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
    def parse(cls, row: str) -> "Ticket":
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

tickets: List[Ticket] = []
for row in inputBlocks[2].splitlines():
    if "ticket" in row:
        continue

    tickets.append(Ticket.parse(row))

myTicket = Ticket.parse(inputBlocks[1].splitlines()[1])

errorRate = 0
invalidMap: Dict[str, Set[int]] = {r.name: set() for r in rules}
for ticket in tickets:
    err = ticket.check(rules)
    if err == 0:
        ticket.setinvalidMap(rules, invalidMap)
    errorRate += err

print(f"part 1: {errorRate}")

cols = list(range(len(tickets[0].numbers)))
unmappedFields = [r.name for r in rules]
fieldMap = {}
while len(unmappedFields) > 1:
    for key in invalidMap:
        if len(invalidMap[key]) == len(unmappedFields) - 1:
            validCol = [c for c in cols if c not in invalidMap[key]][0]
            fieldMap[key] = validCol
            cols.remove(validCol)
            unmappedFields.remove(key)

departures = 1
for col in fieldMap:
    if "departure" in col:
        departures *= myTicket.numbers[fieldMap[col]]

print(f"part 2: {departures}")
