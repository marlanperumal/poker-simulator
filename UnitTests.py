import unittest
from Card import Card
from Deck import Deck


class TestCard(unittest.TestCase):

    def setUp(self):
        self.Ace = Card(1, 1)
        self.Two = Card(2, 2)
        self.Queen = Card(12, 3)
        self.King = Card(13, 4)

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
        hand = deck.deal(5)

card_suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
deck_suite = unittest.TestLoader().loadTestsFromTestCase(TestDeck)
all_tests = unittest.TestSuite([
    card_suite,
    deck_suite
])
unittest.TextTestRunner(verbosity=2).run(all_tests)
