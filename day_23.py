from collections import deque

input = "614752839"

rounds = 100

input = "389125467"
rounds = 10

circle = deque([int(i) for i in input])


def move():
    current = circle[0]
    circle.rotate(-1)
    inHand = [circle.popleft() for _ in range(3)]
    print(inHand)
    circle.rotate(1)

    index = None
    while index is None:
        current -= 1
        try:
            index = circle.index(current)
        except:
            pass
        if current < 0:
            current = max(circle)

    for i, e in enumerate(inHand):
        circle.insert(index + i + 1, e)

    circle.rotate(-1)


for i in range(rounds):
    circle.rotate(i)
    print(circle)
    circle.rotate(-i)
    move()
