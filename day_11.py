import utils

input = utils.getInput(11)

orgState = [[s for s in row] for row in input.splitlines()]


def occupied(state, x, y, inview):
    c = 0
    for mx in [-1, 0, 1]:
        for my in [-1, 0, 1]:
            _x = x + mx
            _y = y + my

            if _x == x and _y == y:
                continue

            try:
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
            if col == "L" and occ == 0:
                newState[x][y] = "#"
            elif col == "#" and occ >= tolerance:
                newState[x][y] = "L"

    return newState


def getSeats(state, tolerance, inview):
    currentState = [r[:] for r in state]
    while True:
        nextState = doFrame(currentState, tolerance, inview)
        if nextState == currentState:
            break
        currentState = nextState

    return sum([r.count("#") for r in currentState])


print(f"part 1: {getSeats(orgState, 4, False)}")
print(f"part 2: {getSeats(orgState, 5, True)}")
