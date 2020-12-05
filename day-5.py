import utils

input = utils.getInput(5).split("\n")

ROWS = 128
COLS = 8


def splitList(listToSplit):
    half = len(listToSplit) // 2
    return listToSplit[:half], listToSplit[half:]


def calcSeat(seat):
    posRows = [i for i in range(ROWS)]
    posCols = [i for i in range(COLS)]
    for letter in seat:
        if letter == "F":
            posRows, _ = splitList(posRows)
        elif letter == "B":
            _, posRows = splitList(posRows)
        elif letter == "L":
            posCols, _ = splitList(posCols)
        elif letter == "R":
            _, posCols = splitList(posCols)
        else:
            raise Exception(f"Unknow char: {letter}")

    if len(posRows) != 1:
        raise Exception(f"Too many rows left: {posRows}")

    if len(posCols) != 1:
        raise Exception(f"Too many cols left: {posCols}")

    return (posRows[0] * 8) + posCols[0]


foundSeats = []
highSeat = 0
for seat in input:
    try:
        seatID = calcSeat(seat)
    except Exception as e:
        raise Exception(f"Error with seat {seat}\n{e}")

    currentSeat = calcSeat(seat)
    highSeat = max(highSeat, currentSeat)
    foundSeats.append(currentSeat)

print(f"part 1: {highSeat}")

emptySeats = []
for i in foundSeats:
    if i + 1 not in foundSeats and i + 2 in foundSeats:
        emptySeats.append(i + 1)

if len(emptySeats) == 1:
    print(f"part 2: {emptySeats[0]}")
else:
    raise Exception(f"Incorect number of empty seats found: {emptySeats}")
