from collections import defaultdict
from typing import DefaultDict, Dict, List, Set

import utils

input = utils.getInput(21)

ingredients: Set[str] = set()
allergens: DefaultDict[str, DefaultDict[str, int]] = defaultdict(
    lambda: defaultdict(lambda: 0)
)
allergenCount: DefaultDict[str, int] = defaultdict(lambda: 0)
seen: DefaultDict[str, int] = defaultdict(lambda: 0)

for l in input.replace("(contains", "|").replace(")", "").splitlines():
    _insStr, _als = l.split("|")

    _ins = _insStr.strip().split(" ")
    for _in in _ins:
        seen[_in] += 1
    for _al in _als.strip().split(", "):
        for _in in _ins:
            allergens[_al][_in] += 1
            ingredients.add(_in)
        allergenCount[_al] += 1

contains: DefaultDict[str, List[str]] = defaultdict(lambda: [])
isIn: DefaultDict[str, Set[str]] = defaultdict(lambda: set())
hasAllergen = []
for allergen in allergens:
    for ingredient in allergens[allergen]:
        if allergens[allergen][ingredient] == allergenCount[allergen]:
            contains[ingredient].append(allergen)
            isIn[allergen].add(ingredient)
            hasAllergen.append(ingredient)


def getDefinitiveContains() -> Dict[str, str]:
    definitiveContains = {}
    while isIn:
        for allergen, ingredient in list(isIn.items()):
            if len(ingredient) == 1:
                definitiveContains[allergen] = min(ingredient)
                del isIn[allergen]
            else:
                isIn[allergen] -= set(definitiveContains.values())

    return definitiveContains


definitiveContains = getDefinitiveContains()

allergenFree = set()
for ingredient in ingredients:
    if ingredient not in hasAllergen:
        allergenFree.add(ingredient)

count = 0
for aFree in allergenFree:
    count += seen[aFree]

print(f"part 1: {count}")
print(f"part 2: {','.join([v for k,v in sorted(definitiveContains.items())])}")
