import utils

input = utils.getInput(11)


currentState = []
for row in input.splitlines():
    r = []
    for col in row:
        r.append(col)
    currentState.append(r)
rowCount = len(currentState)
colCount = len(currentState[0])

# for row in input:
#     for col in row:
#         state.append([col.strip()])


def occupied(state, x, y):
    c = 0
    for mx in [-1, 0, 1]:
        for my in [-1, 0, 1]:
            _x = x + mx
            _y = y + my
            if _x == x and _y == y:
                continue
            if _x < 0 or _y < 0:
                continue
            try:
                if state[_x][_y] == "#":
                    c += 1
            except IndexError:
                pass
    return c


def doFrame(state):
    newState = [r[:] for r in state]
    for x, row in enumerate(state):
        for y, col in enumerate(row):
            occ = occupied(state, x, y)
            if col == "L":
                if occ == 0:
                    newState[x][y] = "#"
            elif col == "#":
                if occ >= 4:
                    newState[x][y] = "L"

    return newState


def draw(state):
    for row in state:
        print("".join(row))
    print("\n")


while True:
    # draw(currentState)
    nextState = doFrame(currentState)
    if nextState == currentState:
        break
    currentState = nextState

seatsTaken = 0
for i in currentState:
    for j in i:
        if j == "#":
            seatsTaken += 1

print(f"part 1: {seatsTaken}")
