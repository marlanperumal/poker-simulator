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
        self.trick_type = trick_type
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

    def __init__(self, cards=None, final_hand_size=5):
        self.final_hand_size = final_hand_size
        if cards is not None:
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
        if self.rank.trick_type != other.rank.trick_type:
            return False
        else:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card.rank_id != other_card.rank_id:
                    return False
            return True

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if Hand.hand_rank.index(self.rank.trick_type) < Hand.hand_rank.index(other.rank.trick_type):
            return True
        elif Hand.hand_rank.index(self.rank.trick_type) > Hand.hand_rank.index(other.rank.trick_type):
            return False
        else:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card.rank_id < other_card.rank_id:
                    return True
                elif self_card.rank_id < other_card.rank_id:
                    return False
            return False

    def __gt__(self, other):
        return not (self < other or self == other)

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
        self.cards.sort()
        self.sorted = True

    def set_card_ranks(self):
        if not self.sorted:
            self.sort()
        for card in self:
            if card.rank in self.card_ranks:
                self.card_ranks[card.rank].append(card)
            else:
                self.card_ranks[card.rank] = [card]

    def set_card_suits(self):
        if not self.sorted:
            self.sort()
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
                singles.append(cards)
            elif len(cards) == 2:
                pairs.append(cards)
            elif len(cards) == 3:
                trips.append(cards)
            elif len(cards) == 4:
                quads.append(cards)

        if len(singles) > 0:
            trick_cards = singles[-1]
            card_rank = trick_cards[0].rank_id
            i = 0
            while len(trick_cards) < 5:
                i -= 1
                if self.cards[i].rank_id != card_rank:
                    trick_cards.append(self.cards[i])
            self.tricks["High Card"] = Trick("High Card", trick_cards)

        if len(pairs) > 0:
            trick_cards = singles[-1]
            card_rank = trick_cards[0].rank_id
            i = 0
            while len(trick_cards) < 5:
                i -= 1
                if self.cards[i].rank_id != card_rank:
                    trick_cards.append(self.cards[i])
            self.tricks["Pair"] = Trick("Pair", trick_cards)

        if len(trips) > 0:
            trick_cards = singles[-1]
            card_rank = trick_cards[0].rank_id
            i = 0
            while len(trick_cards) < 5:
                i -= 1
                if self.cards[i].rank_id != card_rank:
                    trick_cards.append(self.cards[i])
            self.tricks["Trip"] = Trick("Trip", trick_cards)

        if len(quads) > 0:
            trick_cards = singles[-1]
            card_rank = trick_cards[0].rank_id
            i = 0
            while len(trick_cards) < 5:
                i -= 1
                if self.cards[i].rank_id != card_rank:
                    trick_cards.append(self.cards[i])
            self.tricks["Quad"] = Trick("Quad", trick_cards)

        if len(pairs) >= 2:
            high_pair = pairs[-1]
            low_pair = pairs[-2]
            high_card_rank = high_pair[0].rank_id
            low_card_rank = low_pair[0].rank_id
            trick_cards = high_pair + low_pair
            i = 0
            while len(trick_cards) < 5:
                i -= 1
                if self.cards[i].rank_id != high_card_rank and self.cards[i].rank_id != low_card_rank:
                    trick_cards.append(self.cards[i])
            self.tricks["Two Pair"] = Trick("Two Pair", trick_cards)

        if len(pairs) >= 1 and len(trips) >=1:
            pair = pairs[-1]
            trip = pairs[-2]
            trick_cards = trip + pair
            self.tricks["Full House"] = Trick("Full House", trick_cards)

    def check_straight_flush(self):
        for suit in self.card_suits:
            cards = self.card_suits[suit]
            if len(cards) >= 5:
                card_run = []
                if cards[-1].rank == "Ace" and cards[0].rank == "Two":
                    card_run.append(cards[-1])

                card_run.append(cards[0])
                for card in cards[1:]:
                    if card.rank_id == card_run[-1].rank_id + 1:
                        card_run.append(card)
                    elif card.rank_id > card_run[-1].rank_id + 1:
                        if len(card_run) >= 5:
                            self.tricks["Straight Flush"] = Trick("Straight Flush", card_run[-5:])
                            break
                        else:
                            card_run = [card]
                if len(card_run) >= 5:
                    self.tricks["Straight Flush"] = Trick("Straight Flush", card_run[-5:])

    def check_flush(self):
        for suit in self.card_suits:
            cards = self.card_suits[suit]
            if len(cards) >= 5:
                self.tricks["Flush"] = Trick("Flush", cards[-5:])

    def check_straight(self):
        card_run = []
        if "Ace" in self.card_ranks and "Two" in self.card_ranks:
            card_run.append(self.cards[-1])

        card_run.append(self.cards[0])
        for card in self.cards[1:]:
            if card.rank_id == card_run[-1].rank_id + 1:
                card_run.append(card)
            elif card.rank_id > card_run[-1].rank_id + 1:
                if len(card_run) >= 5:
                    self.tricks["Straight"] = Trick("Straight", card_run[-5:])
                    break
                else:
                    card_run = [card]
        if len(card_run) >= 5:
            self.tricks["Straight"] = Trick("Straight", card_run[-5:])

    def calc_rank(self):
        if not self.sorted:
            self.sort()
        self.set_card_ranks()
        self.set_card_suits()
        self.check_straight_flush()
        self.check_flush()
        self.check_straight()
        self.check_duplicates()
        for rank in reversed(Hand.hand_rank):
            if rank in self.tricks:
                self.rank = self.tricks[rank]
                break



