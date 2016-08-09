from Card import Card

class Trick(object):
    # Convention
    # High Card: Cards in descending order
    # Pair: Pair, then kickers in descending order
    # Two Pair: High Pair, Low Pair then kicker
    # Trip: Trip, then kickers in descending order
    # Straight: Cards in descending order
    # Flush: Cards in descending order
    # Full House: Trip then pair
    # Quad: Quad then kicker
    # Straight Flush: Cards in descending order
    def __init__(self, trick_type, cards):
        self.type = trick_type
        self.cards = cards


class Hand(object):
    hand_rank = [
        "High Card",
        "Pair",
        "Two Pair",
        "Trip",
        "Straight",
        "Flush",
        "Full House",
        "Quad",
        "Straight Flush"
    ]

    def __init__(self, cards=None, max_size=5):
        self.max_size = max_size
        if cards is not None and len(cards) < max_size:
            self.cards = cards
        else:
            self.cards = []
        self.card_ranks = {}
        self.card_suits = {}
        self.tricks = {}
        self.rank = None
        self.sort()
        self.sorted = True


    def __repr__(self):
        return self.cards.__repr__()

    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        return self._next()

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def _next(self):
        for card in self.cards:
            yield card

    def copy(self):
        hand = Hand([card.copy() for card in self.cards])
        hand.calc_rank()
        return hand

    def size(self):
        return len(self.cards)

    def add_card(self, card):
        if self.size() < self.max_size:
            self.cards.append(card)
        self.sort()

    def play_card(self, card_num):
        return self.cards.pop(card_num)

    def sort(self):
        self.cards = self.cards.sort()
        self.sorted = True

    def set_card_ranks(self):
        for card in self:
            if card.rank in self.card_ranks:
                self.card_ranks[card.rank].append(card)
            else:
                self.card_rank[card.rank] = [card]

    def set_card_suits(self):
        for card in self:
            if card.suit in self.card_suits:
                self.card_suits[card.suit].append(card)
            else:
                self.card_suits[card.suit] = [card]

    def check_duplicates(self):
        singles = []
        pairs = []
        trips = []
        quads = []

        for rank in self.card_ranks:
            cards = self.card_ranks[rank]
            if len(cards) == 1:
                singles.append(Trick(cards, []))
            elif len(cards) == 2:
                pairs.append(Trick(cards, []))
            elif len(cards) == 3:
                trips.append(Trick(cards, []))
            elif len(cards) == 4:
                quads.append(Trick(cards, []))

        if len(quads) == 1:
            kicker_list =


    def is_straight(self):
        if not self.sorted:
            self.sort()
        rank_id = self.cards[0].rank_id
        for card in self.cards[1:]:
            if card.rank_id is not rank_id + 1:
                return False
            rank_id += 1
        return True

    def is_pair(self):
        if not self.sorted:
            self.sort()
        rank_id = self.cards[0].rank_id
        for card in self.cards[1:]:
            pass

    def check_straight_flush(self):
        if self.is_flush() and self.is_straight():
            self.tricks["Straight Flush"] = Trick(self.cards[-1], [])

    def check_flush(self):
        for suit in self.card_suits:
            cards = self.card_suits[suit]
            if len(cards) >= 5:
                self.tricks["Flush"] = Trick(cards[-5:])

    def check_straight(self):
        if self.is_straight():
            self.tricks["Straight"] = Trick(self.cards[-1], [])

    def check_quad(self):
        if not self.sorted:
            self.sort()


    def calc_rank(self):
        self.check_straight_flush()
        self.check_quad()
        self.check_full_house()
        self.check_flush()
        self.check_straight()
        self.check_trips()
        self.check_two_pair()
        self.check_pair()
        self.check_high_card()



