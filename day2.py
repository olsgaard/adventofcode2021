test1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def step(depth, horizontal, command):
    direction, distance = command.split()
    distance = int(distance)

    if direction == "forward":
        horizontal += distance
    if direction == "down":
        depth += distance
    if direction == "up":
        depth -= distance

    return depth, horizontal

def move(commands):
    depth, horizontal = 0,0
    for command in commands:
        depth, horizontal = step(depth, horizontal, command)

    return depth * horizontal

assert move(test1.split('\n')) == 150

with open('input_day2.txt') as f:
    commands = f.readlines()

print(move(commands))

test2 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def step_aim(depth, horizontal, aim, command):
    direction, distance = command.split()
    distance = int(distance)

    if direction == "forward":
        horizontal += distance
        depth += aim * distance
    if direction == "down":
        aim += distance
    if direction == "up":
        aim -= distance

    return depth, horizontal, aim

def move_aim(commands):
    depth, horizontal, aim = 0,0,0

    for command in commands:
        depth, horizontal, aim = step_aim(depth, horizontal, aim, command)

    return depth * horizontal

assert move_aim(test2.split('\n')) == 900

print(move_aim(commands))
