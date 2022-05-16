test1 = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

bingo_game = test1

def parse_board(board):
	parsed_board = []
	for line in board.split('\n'):
		parsed_board.append([int(n) for n in line.strip().replace('  ', ' ').replace('  ', ' ').split(' ')])
	return parsed_board


def parse_bingo(bingo_game):
	raw_numbers, *raw_boards = bingo_game.split('\n\n')

	numbers = [int(n) for n in raw_numbers.split(',')]
	boards = [parse_board(board) for board in raw_boards]
	markings = [[[False] * 5 for i in range(5)] for b in boards]

	return numbers, boards, markings

numbers, boards, markings = parse_bingo(test1)

def play_bingo(numbers, boards, markings):
	for draw in numbers:
		for marks, board in zip(markings, boards):
			for row_idx, row in enumerate(board):
				try:
					marks[row_idx][row.index(draw)] = True
					if sum(marks[row_idx]) == 5:
						return board, marks, draw
				except ValueError:
					pass

def solve(bingo_game):
	win_board, win_marks, winning_draw = play_bingo(*parse_bingo(bingo_game))

	tally = sum(
		[number 
			for board_row, marks_row in zip(win_board, win_marks) 
			for mark, number in zip(marks_row, board_row) 
			if mark == False
		]
	)

	return tally * winning_draw

assert solve(test1) == 4512 

with open('input_day4.txt') as f:
	bingo_game = f.read().strip()

print(solve(bingo_game))