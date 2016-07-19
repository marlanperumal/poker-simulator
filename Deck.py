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

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        self.shuffled = True

    def sample_one(self):
        return self.sample()[0]

    def sample(self, num_cards):
        return random.sample(self.cards, num_cards)

    def deal_one(self):
        if not self.shuffled:
            self.shuffle()
        return self.cards.pop()

    def deal(self, num_cards):
        if not self.shuffled:
            self.shuffle()
        cards = self.cards[-num_cards:]
        self.cards = self.cards[:len(self.cards)-num_cards]
        return cards


if __name__ == "__main__":
    deck = Deck()
    print(deck.deal_one())
    print(deck.size())
    print(deck.deal(2))
    print(deck.size())
    hand = deck.deal(2)
    print(hand)
    hand = [Card(1, 1), Card(1, 2)]
    print(hand)
    print(hand[0] < hand[1])
    print(hand[0] <= hand[1])
    print(hand[0] > hand[1])
    print(hand[0] >= hand[1])
    print(hand[0] == hand[1])
    print(hand[0] != hand[1])
    hand = deck.deal(5)
    print(hand)
    hand.sort()
    print(hand)
    hand.sort(reverse=True)
    print(hand)

