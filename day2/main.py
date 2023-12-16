"""
Part 1:
Determine which games would have been possible if the bag had been loaded
with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
of the IDs of those games?

Part 2:
For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""
import re

N_RED_CUBES = 12
N_GREEN_CUBES = 13
N_BLUE_CUBES = 14
TOTAL_CUBES = N_RED_CUBES + N_GREEN_CUBES + N_BLUE_CUBES


with open("./input.csv", mode="r") as f:
    game_sets = []
    for line in f.readlines():
        line_data = re.split(": |; ", line[0:-1])
        game_sets.append(line_data[1:])

    possible_games = []
    game_power = []
    for game_id, sets in enumerate(game_sets):
        valid_game = True
        set_dict = dict(n_red=[1], n_blue=[1], n_green=[1])
        for game_set in sets:
            n_red: int = 0
            n_blue: int = 0
            n_green: int = 0
            all_cubes = re.split(" |, ", game_set)
            for i, element in enumerate(all_cubes):
                match element:
                    case "red":
                        n_red = int(all_cubes[i-1])
                        set_dict["n_red"].append(n_red)
                    case "blue":
                        n_blue = int(all_cubes[i-1])
                        set_dict["n_blue"].append(n_blue)
                    case "green":
                        n_green = int(all_cubes[i-1])
                        set_dict["n_green"].append(n_green)

        # PART 1
            if (
                (n_red > N_RED_CUBES) | (n_blue > N_BLUE_CUBES) | (
                    n_green > N_GREEN_CUBES)
            ):
                valid_game = False

        min_dict = dict(min_red=max(set_dict["n_red"]),
                        min_blue=max(set_dict["n_blue"]),
                        min_green=max(set_dict["n_green"]),
                        )
        power = min_dict["min_red"] * \
            min_dict["min_blue"] * min_dict["min_green"]
        game_power.append(power)
        if valid_game:
            possible_games.append(game_id + 1)
    print(f"Answer to part 1: {sum(possible_games)}")
    print(f"Answer to part 2: {sum(game_power)}")
