"""
"""
from statistics import mean

test1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split()

def bit_at_index(string_of_bits, idx):
	""" bits are 0-indexed from right to left, e.g.:

	    string of bits: 010011
	           indices: 543210
	"""

	i = int(string_of_bits, 2)

	# bit-wise AND operation on the 2 to the power of the index
	# turns off all bits, except for the bit at index.
	# if the value is more then 1, the bit at index was set from the get-go
	return i & 2**idx > 0

assert bit_at_index('1', 0) == True
assert bit_at_index('0', 0) == False
assert bit_at_index('1', 1) == False
assert bit_at_index('11', 0) == True
assert bit_at_index('101', 1) == False
assert bit_at_index('100101011', 0) == True
assert bit_at_index('101010101', 1) == False
assert bit_at_index('100101011', 3) == True
assert bit_at_index('101010101', 5) == False

def find_gamma(diagnostic_report, nbits):
	gamma = []

	for i in range(nbits):
		gamma.append(str(round(mean(bit_at_index(number, i) for number in diagnostic_report))))
	gamma.reverse()

	return(int(''.join(gamma), 2))

assert find_gamma(test1, 5) == 22

def find_epsilon(gamma, nbits):
	""" Epsilon has all the bits flipped, compared to gamma. If we simply flip all bits 
	we will end up with a negative number. We also need to take into account that gamma may
	not have all n-bits. So we flip by exclusive-OR against the largest n-bit numbers. That 
	way all leading zeros in gamma becomes 1s, and all 1s become zeros """

	max_nbit = 2**(nbits)-1
	return gamma^max_nbit

assert find_epsilon(22, 5) == 9

def solve1(diagnostic_report, nbits):
	gamma = find_gamma(diagnostic_report, nbits)
	epsilon = find_epsilon(gamma, nbits)

	return gamma * epsilon

with open('input_day3.txt') as f:
	diagnostic_report = f.readlines()

print(solve1(diagnostic_report, 12))

def flip_bit(bit):
	return bit^1

def round(n):
	i = int(n)
	if n >= i + 0.5:
		return i+1
	else:
		return i

def most_common_bit_at_position(pos, numbers):
	""" Confusingly, position is the oppersite of bit index, e.g:

		bits    	1010101
		position 	1234567
	"""
	return round(mean(bit_at_index(number[::-1], pos-1) for number in numbers))

def least_common_bit_at_position(pos, numbers):
	''' return the opposite of `most_common_biy_at_position` '''

	return int(most_common_bit_at_position(pos, numbers) == 0)

def find_rating(rating_type, diagnostic_report, nbits):
	if rating_type == 'oxygen':
		bit_at_position = most_common_bit_at_position
	elif rating_type == 'co2':
		bit_at_position = least_common_bit_at_position
	else:
		raise ValueError('`rating_type` must be set')

	gamma = ''
	numbers = diagnostic_report.copy()
	for pos in range(1, nbits+1):
		gamma += str(bit_at_position(pos, numbers))
		numbers = [n for n in numbers if n.startswith(gamma)]
		if len(numbers) == 1:
			return numbers[0]
		if len(numbers) == 0:
			raise ValueError(f"Ran out of compatible numbers in diagnostic_report. Gamma={gamma}")

assert find_rating('oxygen', test1, 5) == '10111'
assert find_rating('co2', test1, 5) == '01010'

def solve2(diagnostic_report, nbits):
	oxygen_rating = find_rating('oxygen', diagnostic_report, nbits)
	co2_rating = find_rating('co2', diagnostic_report, nbits)

	return int(oxygen_rating, 2) * int(co2_rating, 2)

assert solve2(test1, 5) == 230

print(solve2(diagnostic_report, 12))