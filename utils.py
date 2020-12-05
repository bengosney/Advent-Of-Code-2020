import os


def getInput(day: int) -> list:
    with open(os.path.join("inputs", f"day-{day}.txt")) as f:
        return f.read().strip()
