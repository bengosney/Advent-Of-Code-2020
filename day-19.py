import re

import utils

input = utils.getInput(19)

rawRules, inputLines = input.split("\n\n")


class Rules:
    def __init__(self, rules: str) -> None:
        self.rules = {}
        for rule in rules.splitlines():
            id, details = rule.split(":")
            self.rules[int(id)] = details.strip().replace('"', "")

    def compile(self, maxRecursion):
        return self._compile(0, [], maxRecursion)

    def _compile(self, id, seen, maxRecursion):
        regexParts = []
        rule = self.rules[id]
        if seen.count(id) <= maxRecursion:
            for p in rule.split("|"):
                ruleRegex = ""
                for r in p.split(" "):
                    if r.isnumeric():
                        ruleRegex += self._compile(int(r), seen[:] + [id], maxRecursion)
                    else:
                        ruleRegex += r
                regexParts.append(ruleRegex)

        regex = "|".join(regexParts)

        if id == 0:
            regex = f"^{regex}$"

        if len(regexParts) > 1:
            return f"(?:{regex})"
        else:
            return regex

    def _getMatching(self, inputLines, maxRecursion):
        regex = self.compile(maxRecursion)
        return [f"{m}" for m in re.finditer(regex, inputLines, re.MULTILINE)]

    def getMatching(self, inputLines):
        maxRecursion = 0
        preResults = []
        curResults = self._getMatching(inputLines, maxRecursion)
        while preResults != curResults:
            preResults = curResults
            maxRecursion += 1
            curResults = self._getMatching(inputLines, maxRecursion)

        return preResults


rules = Rules(rawRules)

matches = rules.getMatching(inputLines)
print(f"part 1: {len(matches)}")

rules.rules[8] = "42 | 42 8"
rules.rules[11] = "42 31 | 42 11 31"

matches = rules.getMatching(inputLines)
print(f"part 2: {len(matches)}")
