from collections import Counter

test = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

test2 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

test2_solution = 5353
test_solutions =[8394,9781,1197,9361,4873,8418,4548,1625,8717,4315]

def parse(digits):
	rows = digits.strip().split('\n')
	data = []
	for row in rows:
		inp, outp = row.split(' | ')
		inp = [d for d in inp.split(' ')]
		outp = [d for d in outp.split(' ')]
		data.append((inp, outp))
	return data

# 1, 4, 7, and 8
segment_count_to_digits = {
	2: 1,
	3: 7,
	4: 4,
	7: 8,
}

def solve1(data):
	c = Counter()
	for _, outp in parse(data):
		for digit in outp:
			nsegments = len(digit)
			try:
				c.update([segment_count_to_digits[nsegments]])
			except KeyError:
				pass
	return sum(c.values())

assert solve1(test) == 26

with open('input_day8.txt') as f:
	raw_data = f.read().strip()

print(solve1(raw_data))

scrable_to_clean = {}

def get_number_by_length(length, scrambled):
	return [set(el) for el in scrambled if len(el) == length]

def parse_line(line):
	line = [set(el) for el in line.strip().replace('|','').split()]
	signal_patterns, output_values = line[:-4], line[-4:]
	return signal_patterns, output_values

def decode_line(line):
	signal_patterns, output_values = parse_line(line)

	one, = get_number_by_length(2, signal_patterns)
	four, = get_number_by_length(4, signal_patterns)
	seven, = get_number_by_length(3, signal_patterns)
	eight = set('abcdefg')

	two_three_five = get_number_by_length(5, signal_patterns)
	three, = [el for el in two_three_five if one.issubset(el)]
	two_five = [el for el in two_three_five if el != three]

	eb = [el - three for el in two_five]

	b, = [el for el in eb if el.issubset(four)]
	e, = [el for el in eb if not el.issubset(four)]

	two, = [el for el in two_five if e.issubset(el)]
	five, = [el for el in two_five if b.issubset(el)]

	six_nine_zero = get_number_by_length(6, signal_patterns)
	nine, = [el for el in six_nine_zero if not e.issubset(el)]
	six_zero = [el for el in six_nine_zero if el != nine]
	zero, = [el for el in six_zero if seven.issubset(el)]
	six, = [el for el in six_zero if el != zero]

	solution = [zero, one, two, three, four, five, six, seven, eight, nine]

	digits = int(''.join([str(solution.index(val)) for val in output_values]))
	return digits

assert decode_line(test2) == test2_solution

def solve(signals):
	return sum([decode_line(line) for line in signals.strip().split('\n')])

assert solve(test) == sum(test_solutions)

print(solve(raw_data))
