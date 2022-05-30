test = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


match_close_to_open = {k: v for k, v in zip(')]}>', '([{<')}
match_open_to_close = {v: k for k, v in match_close_to_open.items()}

opens = set(match_close_to_open.values())
close_to_points = {k: v for k, v in zip(')]}>', [3,57,1197,25137])}

def corruption_score(line):
	open_chunks = []
	for char in line:
		if char in opens:
			open_chunks.append(char)
		elif match_close_to_open[char] == open_chunks[-1]:
			open_chunks.pop()
		else:
			return close_to_points[char]
	return 0

assert corruption_score('{([(<{}[<>[]}>{[]{[(<()>') == 1197
assert corruption_score('[[<[([]))<([[{}[[()]]]') == 3
assert corruption_score('[{[{({}]{}}([{[{{{}}([]') == 57
assert corruption_score('[<(<(<(<{}))><([]([]()') == 3
assert corruption_score('<{([([[(<>()){}]>(<<{{') == 25137

def solve(nav_subsystem):
	return sum(corruption_score(line) for line in nav_subsystem.strip().split('\n'))

assert solve(test) == 26397

autocomplete_scores = {k: v for k, v in zip(')]}>', [1, 2, 3, 4])}

def autocomplete(line):
	open_chunks = []
	for char in line:
		if char in opens:
			open_chunks.append(char)
		elif match_close_to_open[char] == open_chunks[-1]:
			open_chunks.pop()
	return [match_open_to_close[char] for char in reversed(open_chunks)]

assert autocomplete('[({(<(())[]>[[{[]{<()<>>') == list('}}]])})]')
assert corruption_score('[({(<(())[]>[[{[]{<()<>>') == 0
assert autocomplete('[(()[<>])]({[<{<<[]>>(') == list(')}>]})')
assert autocomplete('(((({<>}<{<{<>}{[]{[]{}') == list('}}>}>))))')
assert autocomplete('{<[[]]>}<{[{[{[]{()[[[]') == list(']]}}]}]}>')
assert autocomplete('<{([{{}}[<[[[<>{}]]]>[]]') == list('])}>')

def score_autocomplete(result):
	score = 0
	for char in result:
		score = score * 5 + autocomplete_scores[char]
	return score

assert score_autocomplete('}}]])})]') == 288957
assert score_autocomplete(')}>]})') == 5566
assert score_autocomplete('}}>}>))))') == 1480781
assert score_autocomplete(']]}}]}]}>') == 995444
assert score_autocomplete('])}>') == 294

def solve2(nav_subsystem):
	scores = sorted([score_autocomplete(autocomplete(line)) 
			for line in nav_subsystem.strip().split('\n')
			if corruption_score(line) == 0
		])
	return scores[len(scores)//2]

print(solve2(test))
assert solve2(test) == 288957

with open('input_day10.txt') as f:
	inp = f.read()
	print(solve(inp))
	print(solve2(inp))




