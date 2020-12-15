import utils

input = utils.getInput(15)

memory = [int(i) for i in input.split(",")]
startRound = len(memory)

length = 30000000
length = 2020


def getLastIndex(items, item):
    index = -1
    while True:
        try:
            index = items.index(item, index + 1)
        except ValueError as e:
            if index == -1:
                raise e
            return index


for i in range(startRound, length):
    if memory[i - 1] not in memory[:-1]:
        memory.append(0)
        continue

    index = getLastIndex(memory[:-1], memory[i - 1]) + 1
    memory.append(i - index)

    thing1 = i - index
    thing2 = memory.index(memory[i - 1])
    print(f"index: {thing1} - {thing2}")

print(f"part 1: {memory[2019]}")
print(f"part 2: {memory[-1]}")
