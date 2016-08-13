
class Card(object):
    rank_list = [
        'Joker',
        'Ace',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten',
        'Jack',
        'Queen',
        'King'
    ]

    rank_dict = {rank: index for rank, index in enumerate(rank_list)}

    suit_list = [
        'Wild',
        'Spades',
        'Hearts',
        'Diamonds',
        'Clubs'
    ]

    suit_dict = {suit: index for suit, index in enumerate(suit_list)}

    def __init__(self, rank, suit):
        if type(rank) == int:
            self.rank_id = rank
            self.rank = Card.rank_list[rank]
        else:
            self.rank = rank
            self.rank_id = Card.rank_list.index(rank)

        if type(suit) == int:
            self.suit_id = suit
            self.suit = Card.suit_list[suit]
        else:
            self.suit = suit
            self.suit_id = Card.suit_list.index(suit)
        self.name = self.rank + ' of ' + self.suit

    def copy(self):
        return Card(self.rank_id, self.suit_id)

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.rank_id == other.rank_id and self.suit_id == other.suit_id

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.rank_id == 1:
            return False
        elif self.rank_id != other.rank_id and other.rank_id == 1:
            return True
        else:
            return self.rank_id < other.rank_id

    def __le__(self, other):
        return self < other or self.rank_id == other.rank_id

    def __gt__(self, other):
        if other.rank_id == 1:
            return False
        elif self.rank_id != other.rank_id and self.rank_id == 1:
            return True
        else:
            return self.rank_id > other.rank_id

    def __ge__(self, other):
        return self > other or self.rank_id == other.rank_id

