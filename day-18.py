import utils

input = utils.getInput(18)

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

        if v is not None:
            if op == "+":
                tot += v
            elif op == "*":
                tot *= v
        else:
            op = i

    return tot


def getTotal(line):
    _, fullTree = lex(line)
    return calc(fullTree)


print(f"part 1: {sum([getTotal(l) for l in lines])}")
