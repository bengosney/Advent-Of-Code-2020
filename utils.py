import os


def getInput(day: int) -> list:
    with open(os.path.join(os.path.dirname(__file__), "inputs", f"day-{day}.txt")) as f:
        return f.read().strip()
