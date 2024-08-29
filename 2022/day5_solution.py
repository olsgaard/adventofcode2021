from collections import defaultdict
from typing import Dict, Tuple, List

example_crates = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip("\n")


def parse(x) -> Tuple[Dict[int, List[str]], List[List[int]]]:
    crates, procedures_raw = x.split("\n\n")
    stacks = defaultdict(list)
    for line in reversed(crates.split("\n")[:-1]):
        for i, c in enumerate(line[1::4], 1):
            if c.isalpha():
                stacks[i].append(c)
    procedures = []
    for line in procedures_raw.split("\n"):
        procedures.append([int(d) for d in line.split() if d.isdigit()])

    return stacks, procedures


def move_crates_9000(x):
    stacks, procedures = parse(x)
    for p in procedures:
        n, f, t = p
        for i in range(n):
            stacks[t].append(stacks[f].pop())
    return "".join([item[-1] for item in stacks.values()])


assert move_crates_9000(example_crates) == "CMZ"

with open("day5_input.txt") as f:
    crates_instructions = f.read().strip("\n")

print(move_crates_9000(crates_instructions))

def pop_range(l: list, r: int):
    return l[:-r], l[-r:]


def move_crates_9001(x):
    stacks, procedures = parse(x)
    for p in procedures:
        n, f, t = p
        stacks[f], crates = pop_range(stacks[f], n)
        stacks[t].extend(crates)
    return "".join([item[-1] for item in stacks.values()])

assert move_crates_9001(example_crates) == "MCD",move_crates_9001(example_crates)
print(move_crates_9001(crates_instructions))