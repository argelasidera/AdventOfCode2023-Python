import unittest
from src.day2_cube_conundrum.part1 import cube_conundrum as cube_conundrum_part1
from src.day2_cube_conundrum.part2 import cube_conundrum as cube_conundrum_part2


class TestCubeConundrum(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(cube_conundrum_part1("src/day2_cube_conundrum/text.txt"), 2076)

    def test_part2(self):
        self.assertEqual(cube_conundrum_part2("src/day2_cube_conundrum/text.txt"), 70950)
