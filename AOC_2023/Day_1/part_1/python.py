import os
import re

# 1.Read line by line (separated by /n)
# 2.Search the string of each line
# 3.Get the first number found (from beginning of word)
# 4.Get the last number found (from end of word)
# 5.If only one number then duplicate the number

EXAMPLE_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
EXPECTED_OUTPUT = """
12,
38,
15,
77
"""
EXPECTED_TOTAL = "sum of all numbers in EXPECTED_OUTPUT << 142"

total = 0

# for c in example:
#     if c.isdigit():
#         arr.append(c)
# if len(arr) > 1:
#     sop += arr[0] + arr[-1]
# elif len(arr) == 1:
#     sop += arr[0] + arr[0]
#     sop = int(sop)


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        text_input = file.read()
    return text_input


lines = read_file("../input.txt").split("\n")

for line in lines:
    arr = [c for c in line if c.isdigit()]
    if len(arr) > 1:
        total += int(arr[0] + arr[-1])
    elif len(arr) == 1:
        total += int(arr[0] + arr[0])
    else:
        total += 0


print(total)
