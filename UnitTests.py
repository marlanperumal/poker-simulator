import unittest
from poker_simulator import Card, Deck, Hand


class TestCard(unittest.TestCase):

    def setUp(self):
        self.Ace = Card(1, 1)
        self.Two = Card(2, 2)
        self.Queen = Card(12, 3)
        self.King = Card(13, 4)

    def test_card_init(self):
        ace_of_spades_num = Card(1, 1)
        ace_of_spades_word = Card("Ace", "Spades")
        self.assertEqual(ace_of_spades_num, ace_of_spades_word)

    def test__lt__(self):
        self.assertFalse(self.Ace < self.Two)
        self.assertTrue(self.Two < self.Ace)
        self.assertFalse(self.Ace < self.Ace)
        self.assertFalse(self.Two < self.Two)
        self.assertTrue(self.King < self.Ace)
        self.assertFalse(self.Ace < self.King)
        self.assertFalse(self.King < self.Two)
        self.assertTrue(self.Two < self.King)

    def test__gt__(self):
        self.assertTrue(self.Ace > self.Two)
        self.assertFalse(self.Two > self.Ace)
        self.assertFalse(self.Ace > self.Ace)
        self.assertFalse(self.Two > self.Two)
        self.assertFalse(self.King > self.Ace)
        self.assertTrue(self.Ace > self.King)
        self.assertTrue(self.King > self.Two)
        self.assertFalse(self.Two > self.King)

    def test__le__(self):
        self.assertFalse(self.Ace <= self.Two)
        self.assertTrue(self.Two <= self.Ace)
        self.assertTrue(self.Ace <= self.Ace)
        self.assertTrue(self.Two <= self.Two)
        self.assertTrue(self.King <= self.Ace)
        self.assertFalse(self.Ace <= self.King)
        self.assertFalse(self.King <= self.Two)
        self.assertTrue(self.Two <= self.King)

    def test__ge__(self):
        self.assertTrue(self.Ace >= self.Two)
        self.assertFalse(self.Two >= self.Ace)
        self.assertTrue(self.Ace >= self.Ace)
        self.assertTrue(self.Two >= self.Two)
        self.assertFalse(self.King >= self.Ace)
        self.assertTrue(self.Ace >= self.King)
        self.assertTrue(self.King >= self.Two)
        self.assertFalse(self.Two >= self.King)


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()

    def test_sample(self):
        original_size = self.deck.size()
        sample_size = 3
        sample_card = self.deck.sample()
        sample_cards = self.deck.sample(sample_size)
        self.assertIsInstance(sample_card, Card)
        self.assertEqual(len(sample_cards), sample_size)
        self.assertEqual(self.deck.size(), original_size)
        for card in sample_cards:
            self.assertIsInstance(card, Card)
            self.assertTrue(card in self.deck)

    def test_deal(self):
        original_size = self.deck.size()
        sample_size = 3
        sample_card = self.deck.deal()

        self.assertIsInstance(sample_card, Card)
        self.assertEqual(self.deck.size(), original_size - 1)

        sample_cards = self.deck.deal(sample_size)
        self.assertEqual(len(sample_cards), sample_size)
        self.assertEqual(self.deck.size(), original_size - sample_size - 1)
        for card in sample_cards:
            self.assertIsInstance(card, Card)
            self.assertFalse(card in self.deck)


class TestHand(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = Hand(self.deck.deal(5))

    def test__iter__(self):
        for card1, card2 in zip(self.hand, self.hand.cards):
            self.assertEqual(card1, card2)

    def test_high_card(self):
        hand_1 = Hand([
            Card(3, "Spades"),
            Card(4, "Hearts"),
            Card(8, "Clubs"),
            Card(1, "Spades"),
            Card(12, "Spades"),
            Card(13, "Hearts"),
            Card(2, "Diamonds"),
        ])
        hand_2 = Hand([
            Card(3, "Spades"),
            Card(4, "Hearts"),
            Card(8, "Clubs"),
            Card(1, "Spades"),
            Card(12, "Spades"),
            Card(13, "Hearts"),
            Card(1, "Diamonds"),
        ])
        hand_1.calc_rank()
        hand_2.calc_rank()
        self.assertTrue(hand_1.rank.trick_type == "High Card")
        self.assertFalse(hand_2.rank.trick_type == "High Card")

    def test_pair(self):
        pass

    def test_two_pair(self):
        hand_1 = Hand([
            Card(7, "Diamonds"),
            Card(2, "Hearts"),
            Card(5, "Clubs"),
            Card(2, "Diamonds"),
            Card(4, "Spades"),
            Card(7, "Spades"),
            Card(6, "Diamonds")
        ])
        hand_1.calc_rank()
        self.assertTrue(hand_1.rank.trick_type == "Two Pair")

    def test_trip(self):
        pass

    def test_straight(self):
        pass

    def test_flush(self):
        pass

    def test_full_house(self):
        pass

    def test_quad(self):
        pass

    def test_straight_flush(self):
        pass

    def test_compare_hand_ranks(self):
        pass

if __name__ == "__main__":
    card_suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
    deck_suite = unittest.TestLoader().loadTestsFromTestCase(TestDeck)
    hand_suite = unittest.TestLoader().loadTestsFromTestCase(TestHand)
    all_tests = unittest.TestSuite([
        card_suite,
        deck_suite,
        hand_suite
    ])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
