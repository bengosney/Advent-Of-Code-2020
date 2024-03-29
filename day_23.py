from collections import deque

input = "614752839"

rounds = 100

circle = deque([int(i) for i in input])


def move():
    current = circle[0]
    circle.rotate(-1)
    inHand = [circle.popleft() for _ in range(3)]
    circle.rotate(1)

    current -= 1
    while current in inHand:
        current -= 1
        if current <= 0:
            current = max(circle)

    index = circle.index()

    for i, e in enumerate(inHand):
        circle.insert(index + i + 1, e)

    circle.rotate(-1)


for _ in range(rounds):
    move()

while circle[0] != 1:
    circle.rotate()

circle.popleft()

label = "".join(str(c) for c in circle)
print(f"part 1: {label}")

circle = deque([int(i) for i in input])
for i in range(max(circle) + 1, 1000000):
    circle.append(i)

rounds = 10000000
for _ in range(rounds):
    move()

circle.rotate(-1)
c1 = circle.popleft()
c2 = circle.popleft()

print(f"part 2: {c1 * c2}")
