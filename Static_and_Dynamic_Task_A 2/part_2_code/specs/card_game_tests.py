import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        card = Card("Heart", 1)
        self.assertEqual(True, CardGame.check_for_ace(self, card))

    def test_highest_card(self):
        card1 = Card("Spade", 10)
        card2 = Card("Diamond", 3)
        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        cards = [Card("Heart", 1),Card("Spade", 10), Card("Diamond", 3)]
        self.assertEqual("You have a total of 14", CardGame.cards_total(self, cards))
