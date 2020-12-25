import utils

cardKey, doorKey = 12232269, 19452773


def transformSubject(subjectNumber, loopSize):
    val = 1
    for _ in range(loopSize):
        val = (val * subjectNumber) % 20201227

    return val


def findLoopSize(publicKey, subjectNumber=7):
    key = 1
    loops = 0
    while key != publicKey:
        key = (key * subjectNumber) % 20201227
        loops += 1

    return loops


loopSize = findLoopSize(cardKey)
print(loopSize)

encryptionKey = transformSubject(doorKey, loopSize)
print(f"part 1: {encryptionKey}")
