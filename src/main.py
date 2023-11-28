import random

SUITS = ["Heart", "Diamond", "Spade", "Club"]
VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
          "King"]

DECK = []


def initialise_deck():
    for suit in SUITS:
        for value in VALUES:
            DECK.append((suit, value))


def card_value_to_int(value):
    if value in ["Ace", "Jack", "Queen", "King"]:
        return 10
    else:
        return int(value)


initialise_deck()
print(DECK)
random.shuffle(DECK)
print(DECK)



# checkBust
# hit
# doubleDown, cant double down after first turn
# split if cards are same value, split aces can only double down, split aces + picture = 21, not blackjack
# initialDeal
# stand
# check, blackjack 3 to 2, push
# dealer(playerTotal)
# if dealer gets ace, player can use up to half their stake as insureance, pays 2 to 1
# dealer must draw until >= 17
# sideBets?
