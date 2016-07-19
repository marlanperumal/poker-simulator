from Card import Card

class Hand(object):
    hand_rank = [
        "High Card",
        "Pair",
        "Two Pair",
        "Trip",
        "Straight",
        "Flush",
        "Full House",
        "Quads",
        "Straight Flush",
        "Royal Straight Flush"
    ]

    def __init__(self, cards=None, max_size=5):
        self.max_size = max_size
        if cards is not None and len(cards) < max_size:
            self.cards = cards
        else:
            self.cards = []

    def sort(self):
        self.cards = self.cards.sort()
