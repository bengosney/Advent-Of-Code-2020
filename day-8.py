import utils

input = utils.getInput(8).split("\n")


def run(program):
    acc = 0
    pos = 0
    prev = []

    while True:
        if pos in prev:
            return acc, 1

        if pos >= len(program):
            return acc, 0

        prev.append(pos)
        cmd, val = program[pos].split(" ")
        if cmd == "nop":
            pos += 1
        if cmd == "jmp":
            pos += int(val)
        if cmd == "acc":
            acc += int(val)
            pos += 1


acc = run(input)[0]
acc = run(input)[0]

print(f"part 1: {acc}")

for i in range(len(input)):
    debug = input.copy()
    cmd, val = input[i].split(" ")

    if cmd == "acc":
        continue
    if cmd == "nop":
        debug[i] = f"jmp {val}"
    if cmd == "jmp":
        debug[i] = f"nop {val}"

    acc, looping = run(debug)
    if not looping:
        print(f"part 2: {acc}")
