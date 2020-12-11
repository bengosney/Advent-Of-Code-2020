import utils

input = utils.getInput(11)

currentState = []
for row in input.splitlines():
    r = []
    for col in row:
        r.append(col)
    currentState.append(r)

orgState = [r[:] for r in currentState]

rowCount = len(currentState)
colCount = len(currentState[0])


def occupied(state, x, y, inview):
    c = 0
    for mx in [-1, 0, 1]:
        for my in [-1, 0, 1]:
            try:
                _x = x + mx
                _y = y + my

                if _x == x and _y == y:
                    continue

                while inview and state[_x][_y] == ".":
                    _x += mx
                    _y += my

                if _x < 0 or _y < 0:
                    continue
                if state[_x][_y] == "#":
                    c += 1
            except IndexError:
                pass
    return c


def doFrame(state, tolerance, inview):
    newState = [r[:] for r in state]
    for x, row in enumerate(state):
        for y, col in enumerate(row):
            occ = occupied(state, x, y, inview)
            if col == "L":
                if occ == 0:
                    newState[x][y] = "#"
            elif col == "#":
                if occ >= tolerance:
                    newState[x][y] = "L"

    return newState


def draw(state):
    for row in state:
        print("".join(row))
    print("\n")


while True:
    nextState = doFrame(currentState, 4, False)
    if nextState == currentState:
        break
    currentState = nextState

seatsTaken = 0
for i in currentState:
    for j in i:
        if j == "#":
            seatsTaken += 1

print(f"part 1: {seatsTaken}")

currentState = [r[:] for r in orgState]
while True:
    nextState = doFrame(currentState, 5, True)
    if nextState == currentState:
        break
    currentState = nextState

seatsTaken = 0
for i in currentState:
    for j in i:
        if j == "#":
            seatsTaken += 1

print(f"part 2: {seatsTaken}")
