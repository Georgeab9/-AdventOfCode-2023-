import os
import re


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        text_input = file.read()
    return text_input


lines = read_file("../input.txt").split("\n")


EXAMPLE_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

EXPECTED_OUTPUT = """
29,
83,
24,
42,
14,
76
"""

example = "rxnhdflsqdqglxdmfxlxponeseven4one"

num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

arr_letters = []
arr_numbers = []
total = 0


# NOPE: PROBLEM IS I AM GETTING THE FIRST OCCURENCE OF THE SAME MATCHED NUMBER (ALTHOUGH IT CAN BE BOTH AT BEGINNING AND END)

# for word, number in num_map.items():
#     substring, substr_index = word, example.find(word)
#     digits, digit_index = str(number), example.find(str(number))
#     if substr_index != -1:
#         substring = number
#         arr_letters.append({substring: substr_index})
#     if digit_index != -1:
#         digitd = number
#         arr_numbers.append({digitd: digit_index})

# arr_result = arr_letters + arr_numbers

# sorted_pairs = sorted(
#     (pair for element in arr_result for pair in element.items()), key=lambda x: x[1]
# )
# sorted_keys = [key for key, value in sorted_pairs]

# if len(sorted_keys) > 1:
#     total += int(str(sorted_keys[0]) + str(sorted_keys[-1]))
# elif len(sorted_keys) == 1:
#     total += int(str(sorted_keys[0]) + str(sorted_keys[0]))
# else:
#     total = total

# print(example)
# print(sorted_keys)
# print(total)


def find_and_sum(s, num_map):
    arr_result = []
    total = 0

    for word, number in num_map.items():
        substr_index = s.find(word)
        while substr_index != -1:
            arr_result.append({number: substr_index})
            substr_index = s.find(word, substr_index + 1)

    for number in num_map.values():
        digit_index = s.find(str(number))
        while digit_index != -1:
            arr_result.append({number: digit_index})
            digit_index = s.find(str(number), digit_index + 1)

    sorted_pairs = sorted(
        (pair for element in arr_result for pair in element.items()), key=lambda x: x[1]
    )
    sorted_keys = [key for key, value in sorted_pairs]

    if len(sorted_keys) > 1:
        total = int(str(sorted_keys[0]) + str(sorted_keys[-1]))
    elif len(sorted_keys) == 1:
        total = int(str(sorted_keys[0]) + str(sorted_keys[0]))

    return total


totals = sum([find_and_sum(line, num_map) for line in lines])
print(totals)
