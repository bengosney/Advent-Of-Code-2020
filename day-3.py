import utils

input = utils.getInput(3).split("\n")


def getTrees(slopeX, slopeY):
    trees = 0
    col = 0
    for i in range(0, len(input), slopeY):
        if input[i][col] == "#":
            trees += 1

        col = (col + slopeX) % len(input[i])

    return trees


print(f"part 1: {getTrees(3, 1)}")

part2 = 0
part2 *= getTrees(1, 1)
part2 *= getTrees(3, 1)
part2 *= getTrees(5, 1)
part2 *= getTrees(7, 1)
part2 *= getTrees(1, 2)

print(f"part 2: {part2}")
