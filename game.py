import math as m
import random

class Card:
    def __init__(self, colors, value):
        self.colors = colors
        self.value = value

    def __str__(self):
        return f"{self.colors} having value as {self.value}"


class Deck:
    def __init__(self):
        self.card = []
        self.build()

    def build(self):
        colors = ["Red", "Blue", "Green", "Yellow"]
        for color in colors:
            for number in range(10):
                self.card.append(Card(color, str(number)))

    def shuffle(self):
        random.shuffle(self.card)

    def draw(self):
        return self.card.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def show_hand(self):
        print(f"\n{self.name}'s Cards:")
        for i, card in enumerate(self.hand):
            print(i, "-", card)

    def can_play(self, card, top_card):
        return card.colors == top_card.colors or card.value == top_card.value


# Beginning of our mastermind game : 
deck = Deck()
deck.shuffle()

player1 = Player("You")
player2 = Player("Computer")

# seven is lucky one so let's provide seven card : 
for _ in range(7):
    player1.draw_card(deck)
    player2.draw_card(deck)

# Starting card
top_card = deck.draw()
print("Starting Card:", top_card)

# slay till someone wins: 
while True:
    # Turn of the game master(player turn):
    player1.show_hand()
    print("\nTop Card:", top_card)

    choice = int(input("Choose card index: "))
    selected = player1.hand[choice]

    if player1.can_play(selected, top_card):
        top_card = selected
        player1.hand.pop(choice)
        print("You played:", selected)
    else:
        print("Invalid move, you must draw a card.")
        player1.draw_card(deck)

    if len(player1.hand) == 0:
        print("You Win!")
        break

    # Let's give chance to our dear computer bro :
    played = False
    for card in player2.hand:
        if player2.can_play(card, top_card):
            top_card = card
            player2.hand.remove(card)
            print("Computer played:", card)
            played = True
            break

    if not played:
        player2.draw_card(deck)
        print("Computer drew a card")

    if len(player2.hand) == 0:
        print("Computer Wins!")
        break