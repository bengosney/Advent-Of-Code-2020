import utils

input = utils.getInput(22)

inputy = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


class Player:
    def __init__(self, id, cards) -> None:
        super().__init__()

        self.id = id
        self.cards = cards

    @property
    def score(self):
        revCards = self.cards[::-1]
        score = 0
        for i, card in enumerate(revCards, 1):
            score += card * i

        return score

    @classmethod
    def parse(cls, input: str):
        id = None
        cards = []
        for line in input.splitlines():
            if "Player" in line:
                _, id = line.strip(":").split(" ")
            else:
                cards.append(int(line.strip()))

        return cls(int(id), cards)

    def getCard(self):
        c = self.cards[0]
        del self.cards[0]
        return c

    def addCards(self, cards):
        self.cards += cards

    def clone(self, cardCount):
        return Player(self.id, self.cards[:cardCount])

    @property
    def cardsLeft(self) -> int:
        return len(self.cards)

    @property
    def hasCards(self) -> bool:
        return self.cardsLeft > 0


class Combat:
    def __init__(self, p1: Player, p2: Player) -> None:
        super().__init__()

        self.p1 = p1
        self.p2 = p2

    def round(self):
        p1c = self.p1.getCard()
        p2c = self.p2.getCard()
        if p1c > p2c:
            self.p1.addCards([p1c, p2c])
        else:
            self.p2.addCards([p2c, p1c])

        if not self.p1.hasCards:
            return self.p2
        if not self.p2.hasCards:
            return self.p1

        return None

    def play(self):
        winner = None
        while winner is None:
            winner = self.round()

        return winner


class RecursiveCombat(Combat):
    def __init__(self, p1: Player, p2: Player) -> None:
        super().__init__(p1, p2)

        self.previous = []

    def round(self):
        roundState = "|".join(
            [
                ",".join([str(c) for c in self.p1.cards]),
                ",".join([str(c) for c in self.p2.cards]),
            ]
        )
        if roundState in self.previous:
            return self.p1

        self.previous.append(roundState)

        p1c = self.p1.getCard()
        p2c = self.p2.getCard()

        if self.p1.cardsLeft >= p1c and self.p2.cardsLeft >= p2c:
            subGame = RecursiveCombat(self.p1.clone(p1c), self.p2.clone(p2c))
            subWinner = subGame.play()
            if subWinner.id == 1:
                self.p1.addCards([p1c, p2c])
            else:
                self.p2.addCards([p2c, p1c])
        else:
            if p1c > p2c:
                self.p1.addCards([p1c, p2c])
            else:
                self.p2.addCards([p2c, p1c])

        if not self.p1.hasCards:
            return self.p2
        if not self.p2.hasCards:
            return self.p1


parts = input.split("\n\n")
game = Combat(Player.parse(parts[0]), Player.parse(parts[1]))
winner = game.play()
print(f"Player {winner.id} won {game.__class__} with a score of {winner.score}")

game = RecursiveCombat(Player.parse(parts[0]), Player.parse(parts[1]))
winner = game.play()
print(f"Player {winner.id} won {game.__class__} with a score of {winner.score}")
