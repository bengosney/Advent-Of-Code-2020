from collections import defaultdict

import utils

input = utils.getInput(21)

inputy = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

ingredients = set()
allergens = defaultdict(lambda: defaultdict(lambda: 0))
allergenCount = defaultdict(lambda: 0)
seen = defaultdict(lambda: 0)

for l in input.replace("(contains", "|").replace(")", "").splitlines():
    _ins, _als = l.split("|")

    _ins = _ins.strip().split(" ")
    for _in in _ins:
        seen[_in] += 1
    for _al in _als.strip().split(", "):
        for _in in _ins:
            allergens[_al][_in] += 1
            ingredients.add(_in)
        allergenCount[_al] += 1

contains = defaultdict(lambda: [])
isin = defaultdict(lambda: set())
hasAllergen = []
for allergen in allergens:
    for ingredient in allergens[allergen]:
        if allergens[allergen][ingredient] == allergenCount[allergen]:
            contains[ingredient].append(allergen)
            isin[allergen].add(ingredient)
            hasAllergen.append(ingredient)

definitiveContains = {}
while isin:
    for allergen, ingredient in list(isin.items()):
        if len(ingredient) == 1:
            definitiveContains[allergen] = min(ingredient)
            del isin[allergen]
        else:
            isin[allergen] -= set(definitiveContains.values())

allergenFree = set()
for ingredient in ingredients:
    if ingredient not in hasAllergen:
        allergenFree.add(ingredient)

count = 0
for aFree in allergenFree:
    count += seen[aFree]

print(f"part 1: {count}")
print(f"part 2: {','.join([v for k,v in sorted(definitiveContains.items())])}")
