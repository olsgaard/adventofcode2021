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

print(solve2(puzzle))