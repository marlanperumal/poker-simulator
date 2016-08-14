from Card import Card
import random


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit_id in range(1, len(Card.suit_list)):
            for rank_id in range(1, len(Card.rank_list)):
                card = Card(rank_id, suit_id)
                self.cards.append(card)
        self.shuffled = False

    def __contains__(self, item):
        return item in self.cards

    def copy(self):
        deck = Deck()
        deck.shuffled = self.shuffled
        if deck.shuffled:
            deck.cards = [Card(card.rank_id, card.suit_id) for card in self.cards]
        return deck

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        self.shuffled = True

    def sample(self, num_cards=None):
        if num_cards is not None:
            return random.sample(self.cards, num_cards)
        else:
            return self.sample(1)[0]

    def deal(self, num_cards=None):
        if not self.shuffled:
            self.shuffle()

        if num_cards is not None:
            if num_cards == 0:
                cards = []
            else:
                cards = self.cards[-num_cards:]
                self.cards = self.cards[:len(self.cards)-num_cards]
            return cards
        else:
            return self.cards.pop()

    def extract(self, cards):
        self.cards = list(set(self.cards) - set(cards))




