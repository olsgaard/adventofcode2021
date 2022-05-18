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

digits_to_segment_letter = {
	0: 'abcef',
	1: 'cf',
	2: 'acdeg',
	3: 'acdfg',
	4: 'bcdf',
	5: 'abdfg',
	6: 'abdefg',
	7: 'acf',
	8: 'abcdefg',
	9: 'abcdfg',
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

