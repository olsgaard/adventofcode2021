test1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def solve(sonar):
	return sum([current > previous for current, previous in zip(sonar[1:], sonar[:-1]) ])

assert solve(test1) == 7

with open('input_day1.txt') as f:
	puzzle = [int(l) for l in f.readlines()]

print(solve(puzzle))

def solve2(sonar):
	n_pulses = len(sonar)

	return sum([sum(sonar[i+1:i+4]) > sum(sonar[i:i+3]) for i in range(n_pulses-3)])

assert solve2(test1) == 5

def solve2_better(sonar):
	"""As the last two values of `previous`are the same as the two first values of
	`current`, we only need to compare the first value of `previous`to the las value
	of `current` """

	return sum([current > previous for current, previous in zip(sonar[3:], sonar[:-3]) ])

assert solve2_better(test1) == 5

print(solve2_better(puzzle))