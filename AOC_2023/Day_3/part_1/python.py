import os
import re


example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


expected_output = """
Extract the numbers adjacent to a symbol (other than " . "). It can be diagonal, vertical or horizontal.

In the above example: 
467 is adjacent to * because the position of * is at diagonal bottom from 7.
35 is adjacent to * because the position of * is at top from 5.
633 is adjacent to # because the position of # is bottom from 6.
617is adjacent to * because the position of * is right from 7.
592 is adjacent to + because the position of + is diagonal top from 2. 
755 is adjacent to * because the position of * is diagonal bottom from 7. 
664 is adjacent to $ because the position of $ is top from 4. 
598 is adjacent to * because the position of * is top from 5. 

Final result is the sum of all these numbers: 4,361
"""


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        text_input = file.read()
    return text_input


board = read_file("../input.txt").split("\n")

lines = example.split("\n")

arr = []
for line in lines:
    sub_arr = []
    for char in line:
        sub_arr.append(char)
    arr.append(sub_arr)

# for index, char in enumerate(arr[1]):
#     if char.isdigit():
#         char_same_pos = arr[1 + 1][index]
#         char_diagonal_one = arr[1 + 1][index - 1]
#         char_same_diagonal_two = arr[1 + 1][index + 1]

#         if not char_same_diagonal_two.isdigit() and char_same_diagonal_two != ".":
#             # print(char, char_same_diagonal_two)
#             num = ""
#             num_arr = []
#             char_before = arr[1][index - 1]
#             char_after = arr[1][index + 1]

#             if char_before.isdigit():
#                 num_arr += arr[1][:index]
#                 for numb in num_arr:
#                     num += numb

#             if char_after.isdigit():
#                 num += arr[1][index:]
#                 for numb in num_arr:
#                     num += numb

#             num += char

#             print(num)


def is_adjacent_to_symbol(x, y, board):
    rows, cols = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if (
                board[nx][ny] not in [".", " ", "\n", ""]
                and not board[nx][ny].isdigit()
            ):
                return True
    return False


total_sum = 0
for i in range(len(board)):
    j = 0
    while j < len(board[i]):
        if board[i][j].isdigit():
            start_j = j
            while j < len(board[i]) and board[i][j].isdigit():
                j += 1
            number = int(board[i][start_j:j])
            if is_adjacent_to_symbol(i, start_j, board) or is_adjacent_to_symbol(
                i, j - 1, board
            ):
                total_sum += number
        else:
            j += 1

print(total_sum)
