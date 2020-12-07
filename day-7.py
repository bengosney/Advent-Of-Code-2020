import utils
import re

input = utils.getInput(7).split("\n")

class Rule():
    def __init__(self, input) -> None:
        self.colour, contains = input.split(" bags contain ")
        matches = re.finditer(r'(\d\s\w+\s\w+)', contains)
        self.contains = [(int(m.group()[0]), m.group()[1:].strip()) for m in matches]

        
    def __str__(self) -> str:
        return f"{self.colour} = {self.contains}"

    def canContain(self, bag):
        return any([True for c in self.contains if c[1] == bag])

def find(colour):
    return [r for r in rules if r.colour == colour][0]

def mustContain(bag):
    count = 0

    for c in bag.contains:
        count += c[0]
        _bag = find(c[1])
        count += mustContain(_bag) * c[0]
        
    return count

def getContains(colour):
    can = []
    for r in rules:
        if r.canContain(colour):
            can.append(r.colour)
            can += getContains(r.colour)

    return set(can)

rules = [Rule(i) for i in input]
topBag = "shiny gold"

print(f"part 1: {len(getContains(topBag))}")
print(f"part 2: {mustContain(find(topBag))}")
