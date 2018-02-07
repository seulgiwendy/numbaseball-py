from unittest import TestCase

from umpire import Umpire


class TestUmpire(TestCase):

    def test_ball_count(self):
        u = Umpire()
        self.assertEqual(u.ball_count([1, 2, 3], [3, 2, 1]), 2)
        self.assertEqual(u.strike_count([1, 2, 3], [1, 2, 3]), 3)


    def test_strike_count(self):
        self.fail()
