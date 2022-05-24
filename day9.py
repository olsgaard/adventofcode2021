test = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

def adjecent_indices(x,y):
	return (x-1,y), (x+1, y), (x,y+1), (x,y-1)

def get(x, y, heightmap):
	if 0 > min([x, y]):
		return None
	try:
		return int(heightmap[y][x])
	except IndexError:
		return None

def parse(heightmap):
	return [[int(point) for point in line.strip()] for line in heightmap.strip().split('\n')]

def remove_none(iterable):
	return [el for el in iterable if el is not None]

def solve(heightmap):
	heightmap = parse(heightmap)
	low_points = []
	for y, line in enumerate(heightmap):
		for x, point in enumerate(line):
			if point < min(remove_none([get(*xy, heightmap) for xy in adjecent_indices(x,y)])):
				low_points.append(point+1)
	return sum(low_points)

assert solve(test) == 15

with open('input_day9.txt') as f:
	heightmap = f.read()

print(solve(heightmap))

# Find indices of each low point
# Use some sort of floodfill algorith to fill the basin
