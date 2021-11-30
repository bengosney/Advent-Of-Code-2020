import utils

input = utils.getInput(18)

input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
lines = [l.strip() for l in input.replace(" ", "").splitlines()]


def lex(line):
    i = 0
    tree = []
    while i < len(line):
        if line[i].isnumeric():
            tree.append(int(line[i]))
        elif line[i] in "+*":
            tree.append(line[i])
        elif line[i] == "(":
            _i, branch = lex(line[i + 1 :])
            i += _i + 1
            tree.append(branch)
        elif line[i] == ")":
            return i, tree
        i += 1

    return i, tree


def calc(tree):
    tot = 0
    op = "+"
    for i in tree:
        v = None
        if isinstance(i, int):
            v = i

        if isinstance(i, list):
            v = calc(i)

        if v is None:
            op = i

        elif op == "*":
            tot *= v
        elif op == "+":
            tot += v
    return tot


def calc2(tree):
    newTree = tree.copy()

    ops = {
        "+": lambda v1, v2: v1 + v2,
        "*": lambda v1, v2: v1 * v2,
    }

    for op in ops:
        while op in [l for l in newTree if not isinstance(l, list)]:
            i = newTree.index(op)

            v = []
            for j in range(i - 1, i + 2, 2):
                if isinstance(newTree[j], list):
                    v.append(calc2(newTree[j]))
                else:
                    v.append(newTree[j])

            newTree = newTree[: i - 1] + [ops[op](v[0], v[1])] + newTree[i + 2 :]

    return newTree[0]


def getTotal(line):
    _, fullTree = lex(line)
    return calc(fullTree)


def getTotal2(line):
    _, fullTree = lex(line)
    return calc2(fullTree)


print(f'part 1: {sum(getTotal(l) for l in lines)}')
print(f'part 2: {sum(getTotal2(l) for l in lines)}')
