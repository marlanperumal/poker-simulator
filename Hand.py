from Card import Card

class Pair(object):
    def __init__(self, cards):


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
        self.rank = None

    def __repr__(self):
        return self.cards.__repr__()

    def __contains__(self, item):
        return item in self.cards

    def copy(self):
        hand = Hand([card.copy() for card in self.cards])
        hand.calc_rank()
        return hand

    def size(self):
        return len(self.cards)

    def add_card(self, card):
        if self.size() < self.max_size:
            self.cards.append(card)

    def play_card(self, card_num):
        return self.cards.pop(card_num)

    def sort(self):
        self.cards = self.cards.sort()

    def calc_rank(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass
