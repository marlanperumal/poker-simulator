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

    def __init__(self, rank_id, suit_id):
        self.rank_id = rank_id
        self.suit_id = suit_id

        self.rank = Card.rank_list[rank_id]
        self.suit = Card.suit_list[suit_id]
        self.name = self.rank + ' of ' + self.suit

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        if self.rank_id == 1:
            return False
        else:
            return self.rank_id < other.rank_id

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self >= other and self != other

    def __ge__(self, other):
        if self.rank_id == 1:
            return True
        else:
            return self.rank_id > other.rank_id

    def __eq__(self, other):
        return self.rank_id == other.rank_id

    def __ne__(self, other):
        return not self == other


