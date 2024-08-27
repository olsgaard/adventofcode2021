from string import ascii_letters

priorities = {k:v for v, k in enumerate(ascii_letters, 1)}

example_rucksacks = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()

def score_duplicates(x):
    score = 0
    for line in x.split('\n'):
        middle = len(line) // 2
        c1, c2 = set(line[:middle]), set(line[middle:])
        overlaps = c1.intersection(c2)
        for item in overlaps:
            score += priorities[item]
    return score

assert score_duplicates(example_rucksacks) == 157, score_duplicates(example_rucksacks)

with open("day3_input.txt") as f:
    rucksacks = f.read().strip()
    print("score1:", score_duplicates(rucksacks))

def score_group_badges(x):
    score = 0
    lines = x.split('\n')
    for g1,g2,g3 in zip(lines[:-2:3], lines[1:-1:3], lines[2::3]):
        overlaps = set(g1).intersection(g2).intersection(g3)
        assert len(overlaps) == 1, (g1, g2, g3)
        for item in overlaps:
            score += priorities[item]
    return score

assert score_group_badges(example_rucksacks) == 70, score_group_badges(example_rucksacks)

with open("day3_input.txt") as f:
    rucksacks = f.read().strip()
    print("score2:", score_group_badges(rucksacks))