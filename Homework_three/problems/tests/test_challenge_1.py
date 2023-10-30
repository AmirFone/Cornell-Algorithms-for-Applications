import unittest
import sys
sys.path.append("..")

from challenge_1.cards_a import cards_game

class TestChallenge1(unittest.TestCase):
    def test_correctness_challenge_a1(self):
        """Public Test """
        self.assertEqual(cards_game(m=3, k=2, n=3, counts = {
                    1: [(1,2),(3,2)],
                    2: [(1,1), (2,1), (2,2)],
                    3: [(2,2), (3,2)]}),
                    2)
    def test_correctness_challenge_a2(self):
        """Public Test """
        self.assertEqual(cards_game(m=3, k=2, n=3, counts = {
                    1: [(1,2), (2,2), (2,2), (3,2)],
                    2: [(1,1), (2,1)],
                    3: [(3,2)]}),
                    1)