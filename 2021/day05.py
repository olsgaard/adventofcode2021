import re
from collections import Counter

test1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

def parse_input(lines_of_vents: str):
	output = []
	for row in lines_of_vents.strip().split('\n'):
		x1, y1, x2, y2 = [int(n) for n in re.split(r',| -> ', row)]
		output.append([(x1, y1), (x2, y2)])
	return output

def filter_horizontal_and_vertical_lines(lines_of_vents: list):
	vertical_and_horizontal_lines = []
	for line in lines_of_vents:
		(x1, y1), (x2, y2) = line
		if (x1 == x2) or (y1 == y2):
			vertical_and_horizontal_lines.append(line)
	return vertical_and_horizontal_lines

def mark_straight_lines(board, lines):
	for line in lines:
		(x1, y1), (x2, y2) = line
		x1, x2 = sorted([x1,x2])
		y1, y2 = sorted([y1,y2])
		board.update((x,y) for x in range(x1, x2+1) for y in range(y1, y2+1))
	return board

def solve1(lines):
	board = Counter()	
	lines = parse_input(lines)
	lines = filter_horizontal_and_vertical_lines(lines)

	board = mark_straight_lines(board, lines)
	return len([True for value in board.values() if value > 1])

assert solve1(test1) == 5

with open('input_day5.txt') as f:
	raw_lines = f.read().strip()

print(solve1(raw_lines))

def filter_diagonal_lines(lines):
	diagonal_lines = []
	for line in lines:
		(x1, y1), (x2, y2) = line
		if (x1 != x2) and (y1 != y2):
			diagonal_lines.append(line)
	return diagonal_lines

def mark_diagonal_lines(board, lines):
	for line in lines:
		(x1, y1), (x2, y2) = line
		x_direction = 1 if x1 < x2 else -1
		#x1, x2 = sorted([x1,x2])
		y_direction = 1 if y1 < y2 else -1
		#y1, y2 = sorted([y1,y2])
		board.update(
			(x,y) for x, y in zip(
				# In order for `range` to count backwards, we need to give it _both_
				# the reverse order, _and_ a negative step value of -1 (since we want all steps). 
				# When counting backwards, we want to include the end point, by going one step beyond
				# that is, adding the direction to our stop.
				range(x1, x2+x_direction, x_direction), 
				range(y1, y2+y_direction, y_direction)
			)
		)
	return board

def solve2(lines):
	board = Counter()	
	lines = parse_input(lines)
	straight_lines = filter_horizontal_and_vertical_lines(lines)
	diagonal_lines = filter_diagonal_lines(lines)

	board = mark_straight_lines(board, straight_lines)
	board = mark_diagonal_lines(board, diagonal_lines)
	return len([True for value in board.values() if value > 1])

assert solve2(test1) == 12, f"'{solve2(test1)}' is not '12'"

print(solve2(raw_lines))




