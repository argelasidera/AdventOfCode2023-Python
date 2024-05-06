import unittest
from src.day3_gear_ratios.part1 import gear_ratios as gear_ratios_part1
from src.day3_gear_ratios.part2 import gear_ratios as gear_ratios_part2


class TestGearRatios(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(gear_ratios_part1("src/day3_gear_ratios/text.txt"), 533784)

    def test_part2(self):
        self.assertEqual(gear_ratios_part2("src/day3_gear_ratios/text.txt"), 78826761)
