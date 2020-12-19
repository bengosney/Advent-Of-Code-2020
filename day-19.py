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

    def compile(self, id=0):
        regexParts = []
        rule = self.rules[id]
        for p in rule.split("|"):
            ruleRegex = ""
            for r in p.split(" "):
                if r.isnumeric():
                    ruleRegex += self.compile(int(r))
                else:
                    ruleRegex += r
            regexParts.append(ruleRegex)

        regex = "|".join(regexParts)

        if id == 0:
            regex = f"^{regex}$"

        if len(regexParts) > 1:
            return f"({regex})"
        else:
            return regex


rules = Rules(rawRules)
matches = [f"{m}" for m in re.finditer(rules.compile(), inputLines, re.MULTILINE)]

print(f"{len(matches)}")
