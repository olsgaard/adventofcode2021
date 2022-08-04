from copy import deepcopy

mapl = lambda f,i: list(map(f,i))
steps = [[mapl(int,list(line)) for line in board.split()] for board in [
"""11111
19991
19191
19991
11111""",
"""34543
40004
50005
40004
34543""",
"""45654
51115
61116
51115
45654"""
]]

def increase_at(idx, board):
    x,y = idx
    board[y][x] += 1
    if board[y][x] == 10:
        for i in surrounding(idx, board):
            board = increase_at(i, board)
    return board
    
def surrounding(idx: tuple, board:list) -> tuple:
    x,y = idx
    xmax = len(board[0])
    ymax = len(board)

    within_bounds = lambda x,y: (0 <= x < xmax) & (0 <= y < ymax)

    coord_change = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0),         (1, 0),
        (-1, 1), (0, 1), (1, 1),    
    ]

    move_coords = lambda cc: (x + cc[0], y + cc[1])
    new_coords = map(move_coords, coord_change)
    return [coord for coord in new_coords if within_bounds(*coord)]


def step(board):
    board = deepcopy(board)
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            increase_at((x,y), board)

    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            board[y][x] = cell if cell < 10 else 0

    return board

assert step(steps[0]) == steps[1]
assert step(steps[1]) == steps[2]

