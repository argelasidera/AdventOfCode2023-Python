import unittest

from src.scratchcards.part1 import scratchcards as scratchcards_part1
from src.scratchcards.part2 import scratchcards as scratchcards_part2


class TestScratchcards(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(scratchcards_part1("src/scratchcards/text.txt"), 23235)

    def test_part2(self):
        self.assertEqual(scratchcards_part2("src/scratchcards/text.txt"), 5920640)
