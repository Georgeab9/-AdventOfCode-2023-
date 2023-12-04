import os
import re
import itertools


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        text_input = file.read()
    return text_input


lines = read_file("../input.txt").split("\n")


# In game 5, 3 sets are being revealed then put back: first set includes 10 blue, 7 green and 2 red ... separated by " ; "
game_ex = "Game 5: 10 blue, 7 green, 2 red; 2 blue, 4 red; 2 green, 9 blue, 8 red"


GOAL = "The Elf would first like to know which games would have been possible if the bag \
        contained only 12 red cubes, 13 green cubes, and 14 blue cubes?"


EXAMPLES = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# In the examples, game 3 is impossible because 20 red were shown at once and game 4 because 15 blue were shown at once.


example = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"


# Split lines
# For each line, remove everything before ":" and keep the number ID only (since we want to sum later)
# Split each line by delimiter ";" which represent each set
# Create a constraint object for each cube color (red: 12, green: 13, blue: 14)
# Transform 1 green into green : 1 ...
# Compare the value with the constraint object value by matching on keys. If we find that it is > constraint then label as impossible
# Sum all ids which are impossible


def sum_impossible(file):
    ans = 0
    for line in file:
        id, game = line.split(": ")
        for set in game.split("; "):
            colors = [x.split() for x in set.split(", ")]
            counts = {b: int(a) for a, b in colors}
            if not (
                counts.get("red", 0) <= 12
                and counts.get("green", 0) <= 13
                and counts.get("blue", 0) <= 14
            ):
                break
        else:
            ans += int(id.split()[-1])
    return ans


print(sum_impossible(lines))
