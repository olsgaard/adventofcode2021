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
	for row in lines_of_vents:
		x1, y1, x2, y2 = [int(n) for n in re.split(',| -> ', row)]
		output.append([(x1, y1), (x2, y2)])
	return output

def filter_horizontal_and_vertical_lines(lines_of_vents: list):
	return []
