from collections import defaultdict

import utils

input = utils.getInput(6).split("\n\n")

p1 = 0
p2 = 0
for group in input:
    answers = defaultdict(lambda: 0)
    for line in group:
        for char in line.strip():
            answers[char] += 1
    p1 += sum([True for i in answers.values() if i > 0])
    p2 += sum([True for i in answers.values() if i == len(group.splitlines())])

print(f"part 1: {p1}")
print(f"part 2: {p2}")
