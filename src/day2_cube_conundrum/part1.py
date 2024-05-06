from typing import List
import re


def check_if_possible(arr: List[str]) -> bool:
    possible_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for s in arr:
        num_cube_str, color = s.replace("\n", "").split(" ")

        if possible_cubes[color] < int(num_cube_str):
            return False
    else:
        return True


def power_of_cube_sets(arr: List[str]) -> int:
    cubes_products = 0
    cubes_map = {}

    for s in arr:
        num_cube_str, color = s.replace("\n", "").split(" ")
        num_cube = int(num_cube_str)

        if color in cubes_map:
            if cubes_map[color] < num_cube:
                cubes_map[color] = num_cube
        else:
            cubes_map[color] = num_cube

    for cm_keys in cubes_map:
        cubes_products = cubes_map[cm_keys] if cubes_products == 0 else cubes_map[cm_keys] * cubes_products

    return cubes_products


def cube_conundrum(source_file: str):
    with open(source_file) as file:
        possible_count = 0

        for line in file:
            game_no_str, each_sets = line.split(": ")
            arr_nums_colors = re.split("; |, ", each_sets)
            possible = check_if_possible(arr_nums_colors)

            if possible:
                possible_count += int(game_no_str.replace("Game", ""))

        print(possible_count)
        return possible_count


if __name__ == "__main__":
    cube_conundrum("text.txt")
