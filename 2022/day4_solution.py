example_pairs = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()

def read_sections(x):
    start, end = x.split('-')
    return set(range(int(start), int(end)+1))

def read_pairs(x):
    fully_contained_count = 0
    for line in x.split('\n'):
        s1, s2 = [read_sections(s) for s in line.split(",")]
        if s1.issubset(s2) or s2.issubset(s1):
            fully_contained_count += 1
    return fully_contained_count

example_score = read_pairs(example_pairs)
assert example_score == 2, example_score

with open("day4_input.txt") as f:
    print("fully_contained pairs:", read_pairs(f.read().strip()))

def read_pairs_overlap(x):
    intersecting_pair_count = 0
    for line in x.split('\n'):
        s1, s2 = [read_sections(s) for s in line.split(",")]
        if s1.intersection(s2):
            intersecting_pair_count += 1
    return intersecting_pair_count

example_score = read_pairs_overlap(example_pairs)
assert example_score == 4, example_score

with open("day4_input.txt") as f:
    print("Intersecting pairs:", read_pairs_overlap(f.read().strip()))