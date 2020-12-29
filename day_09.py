import utils

input = [int(i) for i in utils.getInput(9).split("\n")]
inputLength = len(input)

preableSize = 25
part1 = None
part2 = None
for i in range(preableSize, inputLength):
    found = False
    for j in range(i - preableSize, i):
        for k in range(i - preableSize, i):
            if input[j] != input[k] and (input[j] + input[k]) == input[i]:
                found = True

    if not found:
        part1 = input[i]
        break

if part1 is None:
    exit(1)

print(f"part 1: {part1}")

for i in range(inputLength):
    for j in range(inputLength):
        if j - i < 2:
            continue

        currentRange = input[i:j]
        rangeSum = sum(currentRange)
        if rangeSum == part1:
            part2 = min(currentRange) + max(currentRange)
            break

        if rangeSum > part1:
            break

    if part2 is not None:
        break

if part2 is None:
    exit(2)

print(f"part 2: {part2}")
