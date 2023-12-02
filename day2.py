# Input loading
with open("aoc_input/day2.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

# Input parsing
game_dict = {}
game_num = 1
for line in puzzle_input:
    set_dict = {}
    set_num = 1
    sets = [string.split(", ") for string in line.split(": ")[1].split("; ")]
    for one_set in sets:
        cube_dict = {}
        for cube in one_set:
            cube_num, cube_col = cube.split(" ")
            cube_dict[cube_col] = int(cube_num)
        set_dict[set_num] = cube_dict
        set_num += 1
    game_dict[game_num] = set_dict
    game_num += 1
puzzle_input = game_dict

# Input exporting
# with open("DAY-2/day-2-data.csv", "w") as f:
#     f.write("GAME;SET;COL;COUNT\n")
#     for game_num, set_dict in game_dict.items():
#         print(set_dict)
#         for set_num, cube_dict in set_dict.items():
#             for cube_col in ["red", "blue", "green"]:
#                 cube_num = cube_dict.get(cube_col, 0)
#                 f.write("{};{};{};{}\n".format(game_num, set_num, cube_col, cube_num)) 

# Functions
def day2_part1(puzzle_input):
    conditions_dict = {"red": 12, "green": 13, "blue": 14}
    solution = 0
    for game_num, set_dict in game_dict.items():
        illegal = False
        for set_num, cube_dict in set_dict.items():
            for cube_col, cube_num in cube_dict.items():
                if cube_num > conditions_dict[cube_col]:
                    illegal = True
        if not illegal:
            solution += game_num
    print("Part 1 Solution: " + str(solution))
    return solution

def day2_part2(puzzle_input):
    solution = 0
    for game_num, set_dict in game_dict.items():
        col_dict = {"red": [], "green": [], "blue": []}
        for set_num, cube_dict in set_dict.items():
            for cube_col, cube_num in cube_dict.items():
                col_dict[cube_col].append(cube_num)
        set_power = max(col_dict["red"]) * max(col_dict["blue"]) * max(col_dict["green"])
        solution += set_power
    print("Part 2 Solution: " + str(solution))
    return solution

# Test Part 1
# if day2_part1(puzzle_input) == 8:
#     print("PASS")
# else:
#     print("FAIL")

# Solution (Part1)
day2_part1(puzzle_input)

# Test Part 2
# if day2_part2(puzzle_input) == 2286:
#     print("PASS")
# else:
#     print("FAIL")

# Solution (Part2)
day2_part2(puzzle_input)
