from collections import deque, Counter
from itertools import islice

from matplotlib.font_manager import fontManager

def sliding_window(iterable, n):
    """ sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    As implemented in itertools recipes: https://docs.python.org/3/library/itertools.html#itertools-recipes"""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield ''.join(tuple(window))
    for x in it:
        window.append(x)
        yield ''.join(tuple(window))

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

def read_input(inp: str):
    start, formula = inp.strip().split('\n\n')
    formula = {x: y for x,y in (line.split(' -> ') for line in formula.strip().split('\n'))}

    return start, formula

def expand_string(string:str, formula:dict):
    return "".join(s[0]+formula[s] for s in sliding_window(string, 2))+string[-1]

start, formula = read_input(test_input)

# tests
assert (step1 := expand_string(start, formula)) == "NCNBCHB"
assert  expand_string(step1, formula) == "NBCCNBBBCBHCB"

def solve(inp: str, n):
    string, formula = read_input(inp)
    for step in range(n):
        string = expand_string(string, formula)
    c = Counter(string).most_common()
    most_common = c[0][1]
    least_common = c[-1][1]
    return most_common - least_common

assert solve(test_input, 10) == 1588 

# Solve puzzle 1

with open("input_day14.txt") as inp:
    # Solve puzzle 1
    inp = inp.read().strip()
    print(solve(inp, 10))
    
    
    # Try to solve puzzle 2
    calculate_time = False
    if calculate_time:
        from timeit import timeit
        for n in range(4, 25):
            print(n, timeit(lambda: solve(inp, n), number=1))
        print("We see time roughly doubles per step. Need to find a less naive solution")



# Puzzle 2

def read_input2(inp: str):
    start, formula = inp.strip().split('\n\n')
    formula = {tuple(x): y for x,y in (line.split(' -> ') for line in formula.strip().split('\n'))}

    return start, formula

def solve2(inp, steps):
    string, formula = read_input2(inp)
    l = list(string)
    for step in range(steps):
        i = 0
        while i+1 < len(l):
            ii = i+2
            l.insert( i+1, formula[tuple(l[i:ii])])
            i =ii
    most_common = Counter(l).most_common()
    return most_common[0][1] - most_common[-1][1]

assert solve2(test_input, 10) == 1588 

with open("input_day14.txt") as inp:
    inp = inp.read().strip()
    
    # Try to solve puzzle 2
    calculate_time = False
    if calculate_time:
        from timeit import timeit
        for n in range(4, 15):
            print(n, timeit(lambda: solve2(inp, n), number=1))
        print("This is slower, and grows faster")

# Use Counters
#
# I felt like this should be solvable with counters, but I was too focused on the order of items
# https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hoib78w/ gave a clear explanation of how to keep counts of things
# without depending on the order of bigrams
#
# The trick is to not think `NN -> NCN` and now I have a loose character
# that is not connected to anything, because I have lost the order of bigrams.
# Instead, store each bigram independently, and convert each bigram to _two_ new
# bigrams. `NN -> NC CN`. this will give you the bigrams needed to expand from step to step
# On top of this we need to keep track of the inital character counts, and add the number of inserted characters at each step. 
# We cannot tally up char counts from the bigram counter at the end, as that would require knowing the order of bigrams

def solve3(inp, steps):
    string, formula = read_input(inp)
    c1 = Counter(sliding_window(string, 2))
    chars = Counter(string)
    for step in range(steps):
        c2 = Counter()
        for (a, b), counts in c1.items():
            c = formula[a+b]
            chars[c] += counts
            c2.update(Counter({a+c: counts, c+b: counts}))
        c1 = c2

    chars = chars.most_common()
    most_common = chars[0][1]
    least_common = chars[-1][1]
    return most_common - least_common        

with open("input_day14.txt") as inp:
    # Solve puzzle 1
    inp = inp.read().strip()
    print(solve3(inp, 10))
    print(solve3(inp, 40))