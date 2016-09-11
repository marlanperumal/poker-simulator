from poker_simulator import Deck, Hand, Card


class HandProbability(object):
    def __init__(self, num_players=None, default_repeats=1000):
        if num_players is None:
            self.num_players = 2
        else:
            self.num_players = num_players
        self.default_repeats = default_repeats

    def run(self, my_hole_cards=None, community_cards=None, repeats=None, verbose=False):
        if repeats is None:
            repeats = self.default_repeats

        if my_hole_cards is None:
            my_hole_cards = []

        if community_cards is None:
            community_cards = []

        record = {
            "win": 0,
            "draw": 0,
            "loss": 0,
            "total": 0
        }

        stack = 0

        for _ in range(repeats):
            result = "win"
            deck = Deck()
            deck.extract(my_hole_cards)
            deck.extract(community_cards)
            deck.shuffle()
            my_cards = my_hole_cards + deck.deal(2 - len(my_hole_cards))
            remaining_community_cards = deck.deal(7 - len(my_cards) - len(community_cards))
            my_hand = Hand(my_cards + community_cards + remaining_community_cards)
            my_hand.calc_rank()
            num_split = 1

            for opponent in range(self.num_players - 1):
                opponent_cards = deck.deal(2)
                opponent_hand = Hand(opponent_cards + community_cards + remaining_community_cards)
                opponent_hand.calc_rank()

                if my_hand < opponent_hand:
                    result = "loss"
                    break
                elif opponent_hand == my_hand:
                    result = "draw"
                    num_split += 1
            record[result] += 1
            record["total"] += 1
            if result == "win":
                stack += self.num_players
            elif result == "draw":
                stack += self.num_players / num_split

        if verbose:
            print("Hand Probability Simulation")
            print("Playing against {} other player(s)".format(self.num_players - 1))
            print("With hand: ", my_hole_cards)
            print("And Community Cards: ", community_cards)
            print("Over {} rounds".format(repeats))
            print("*****************************************")
            print("Win Percentage: {0:.0%}".format(record["win"] / record["total"]))
            print("Draw Percentage: {0:.0%}".format(record["draw"] / record["total"]))
            print("Loss Percentage: {0:.0%}".format(record["loss"] / record["total"]))
            print("Relative Hand Strength: {0:.2f}".format(stack/repeats))

        record["win percentage"] = record["win"] / record["total"]
        record["draw percentage"] = record["draw"] / record["total"]
        record["loss percentage"] = record["loss"] / record["total"]
        record["relative hand strength"] = stack/repeats
        return record

if __name__ == "__main__":
    simulation = HandProbability(num_players=6, default_repeats=100)
    probability_matrix = []
    rank_list = Card.rank_list[2:] + Card.rank_list[1:2]
    for i, rank_1 in enumerate(rank_list):
        print(rank_1)
        unsuited_probability = []
        suited_probability = []
        for rank_2 in rank_list[:i]:
            suited_record = simulation.run(my_hole_cards=[Card(rank_1, "Hearts"), Card(rank_2, "Hearts")])
            suited_probability.append(suited_record["win percentage"] + suited_record["draw percentage"])
        for rank_2 in rank_list[i:]:
            unsuited_record = simulation.run(my_hole_cards=[Card(rank_1, "Hearts"), Card(rank_2, "Spades")])
            unsuited_probability.append(unsuited_record["win percentage"] + unsuited_record["draw percentage"])
        probability_matrix.append(suited_probability + unsuited_probability)
    print(rank_list)
    for rank in range(len(probability_matrix)):
        print(probability_matrix[rank])

