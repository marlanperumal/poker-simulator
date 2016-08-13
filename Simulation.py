from Deck import Deck
from Hand import Hand
from Card import Card


class HandProbability(object):
    def __init__(self, num_opponents=1, default_repeats=1000):
        self.num_opponents = num_opponents
        self.default_repeats = default_repeats

    def run(self, my_cards, community_cards=None, repeats=None):
        if repeats is None:
            repeats = self.default_repeats

        if community_cards is None:
            community_cards = []

        record = {
            "win": 0,
            "draw": 0,
            "loss": 0,
            "total": 0
        }

        for i in range(repeats):
            result = "win"
            deck = Deck()
            deck.extract(my_cards)
            deck.extract(community_cards)
            deck.shuffle()
            remaining_community_cards = deck.deal(7 - len(my_cards) - len(community_cards))
            my_hand = Hand(my_cards + community_cards + remaining_community_cards)
            my_hand.calc_rank()
            for player in range(self.num_opponents):
                hand = Hand(deck.deal(2) + community_cards + remaining_community_cards)
                hand.calc_rank()
                if hand > my_hand:
                    result = "loss"
                    break
                elif hand == my_hand:
                    result = "draw"
            record[result] += 1
            record["total"] += 1

        print("Hand Probability Simulation")
        print("Playing against {} other player(s)".format(self.num_opponents))
        print("With hand: ", my_cards)
        print("And Community Cards: ", community_cards)
        print("Over {} rounds".format(repeats))
        print("*****************************************")
        print("Win Percentage: {0:.0%}".format(record["win"] / record["total"]))
        print("Draw Percentage: {0:.0%}".format(record["draw"] / record["total"]))
        print("Loss Percentage: {0:.0%}".format(record["loss"] / record["total"]))
        print("Relative Hand Strength: {0:.0%}".format(record["win"] / record["total"] * (self.num_opponents+1)))
        return record

if __name__ == "__main__":
    simulation = HandProbability(num_opponents=4, default_repeats=10000)
    record = simulation.run([Card("Queen", "Spades"), Card("Ten", "Hearts")], [Card("Queen", "Diamonds")])