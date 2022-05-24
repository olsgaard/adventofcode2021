from collections import Counter

test1 = "3,4,3,1,2"

def parse(inpt):
	return [int(i) for i in inpt.strip().split(',')]

def grow_fish(fishes, days):
	for day in range(days):
		new_fish = []
		for i, fish in enumerate(fishes):
			if fish == 0:
				fishes[i] = 6
				new_fish.append(8)
			else: 
				fishes[i] -= 1
		fishes = fishes + new_fish
	return fishes

def solve2(fishes, days):
	# See https://skarlso.github.io/2021/12/06/aoc-day6/ for the idea of using a list to keep track of states
	fishes = parse(fishes)
	# Every fish can be in one of nine states. 
	# Use a list to keep track of the number of
	# fish in each state
	states = [0]*9

	# fill in the number of fish in each state at day 0
	for state, count in Counter(fishes).items():
		states[state] = count

	# begin growing fish
	for day in range(days):
		reset = states.pop(0) # by removing first item in list, all other fishes state decrease by 1
		states[6] += reset # Number of fish in state 6 grows by the number of fish leaving state 0
		states.append(reset) # number of fish in state 8 grows by the number of fish leaving state 0

	return sum(states)


def solve1(fishes, days):
	return len(grow_fish(parse(fishes), days))


assert grow_fish(parse(test1), 18) == parse('6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8')
assert solve1(test1, 18) == 26
assert solve1(test1, 80) == 5934

with open('input_day6.txt') as f:
	fishes = f.read().strip()

print(solve1(fishes, 80))


assert solve2(test1, 18) == 26
assert solve2(test1, 80) == 5934

assert solve2(test1, 256) == 26_984_457_539
print(solve2(fishes, 256))



