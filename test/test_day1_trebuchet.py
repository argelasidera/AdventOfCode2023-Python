import unittest
from src.day1_trebuchet.part1 import trebuchet as trebuchet_part1
from src.day1_trebuchet.part2 import trebuchet as trebuchet_part2


class TestTrebuchet(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(trebuchet_part1("src/day1_trebuchet/text.txt"), 54390)

    def test_part2(self):
        self.assertEqual(trebuchet_part2("src/day1_trebuchet/text.txt"), 54277)
