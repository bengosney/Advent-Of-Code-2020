import time
from collections import deque

input = "614752839"

rounds = 100

circle = deque([int(i) for i in input])


def move():
    current = circle[0]
    circle.rotate(-1)
    inHand = [circle.popleft() for _ in range(3)]
    circle.rotate(1)

    index = None
    while index is None:
        current -= 1
        try:
            index = circle.index(current)
        except:
            pass
        if current < 0:
            current = max(circle) + 1

    for i, e in enumerate(inHand):
        circle.insert(index + i + 1, e)

    circle.rotate(-1)


for i in range(rounds):
    move()

while circle[0] != 1:
    circle.rotate()

circle.popleft()

label = "".join([str(c) for c in circle])
print(f"part 1: {label}")

circle = deque([int(i) for i in input])
for i in range(max(circle) + 1, 1000000):
    circle.append(i)


current_millis = lambda: int(round(time.time() * 1000))

startTime = current_millis()
rounds = 10000000
for i in range(rounds):
    if i % 100 == 0:
        try:
            currentTime = current_millis()
            timePer = (currentTime - startTime) // i
            timeLeft = (rounds - i) * timePer
            print(f"left: {rounds - i} - {timeLeft / 60000}")
            exit(0)
        except:
            pass
    move()

circle.rotate(-1)
c1 = circle.popleft()
c2 = circle.popleft()

print(f"part 2: {c1 * c2}")
