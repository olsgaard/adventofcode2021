from collections import namedtuple, defaultdict

test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


Point = namedtuple('Point', ['x', 'y'])
Point.get = Point.__getattribute__


def read_input(inp: str): 
    coords, fold_instructions = inp.strip().split('\n\n')
    coords = {Point(int(x),int(y)) for x, y in (line.strip().split(',') for line in coords.strip().split('\n'))}

    fold_instructions = [(axis[-1], int(val)) for axis, val in (line.split('=') for line in fold_instructions.strip().split('\n'))]

    return coords, fold_instructions

# Fold algorithm:
#
# 00 ...#..#..#. 00
# 01 ....#...... 01
# 02 ........... 02
# 03 #.......... 03
# 04 ...#....#.# 04
# 05 ........... 05
# 06 ........... 06
# 07 ----------- --
# 08 ........... 06
# 09 ........... 05
# 10 .#....#.##. 04
# 11 ....#...... 03
# 12 ......#...# 02
# 13 #.......... 01
# 14 #.#........ 00
#
# We see that numbers below the fold, get moved to `new_idx = fold - (|idx-fold|)`


def fold_point_at(idx: int, fold: int):
    """Folds a single coordinate `idx` around another coordinate `fold`"""
    return fold - abs(idx-fold)

# Assert that `fold_point_at` converts numbers on lefthand side of schema above into right hand side, for all y-indices.
assert [fold_point_at(i, 7) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]] == [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0] 

def fold( axis: str,pos: int, coords: set):
    """Folds a set of `Point`s around a `pos` on either the `x` or `y` `axis`."""
    assert axis in set('xy')
    other_axis = 'y' if axis == 'x' else 'x'

    # This gets pretty hairy to look at. But creates a new point folded at the axis denoted in `axis`
    new_coords = {Point(**{axis: fold_point_at(point.get(axis), pos), other_axis: point.get(other_axis)}) for point in coords}
    return new_coords

def pretty_print(coords: set):
    width = max(p.x for p in coords)+1
    height = max(p.y for p in coords)+1

    for y in range(height):
        print(''.join('#' if Point(x,y) in coords else ' ' for x in range(width)))

# Tests        
coords, fold_instructions = read_input(test_input)

assert len(first_fold := fold('y', 7, coords)) == 17
assert len(fold('x', 5, first_fold)) == 16

for instruction, result in zip(fold_instructions, [17,16]):
    coords = fold(*instruction, coords)
    assert len(coords) == result
# pretty_print(coords)

# Part 1

with open("input_day13.txt") as raw_input:
    coords, fold_instructions = read_input(raw_input.read())
    first_fold = fold(*fold_instructions[0], coords)
    print(len(first_fold))


# part 2

with open("input_day13.txt") as raw_input:
    coords, fold_instructions = read_input(raw_input.read())
    for instruction in fold_instructions:
        coords = fold(*instruction, coords)
    pretty_print(coords)