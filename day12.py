test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_input2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

test_output = """start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end"""

start="start"
end="end"

paths = []
deadends = {}

def read_graph(s):
    return {frozenset(line.split('-')) for line in s.strip().split('\n')}

def filter_in(cave, graph):
    """Returns a set of all connections containing `cave` in `graph`"""
    return {el for el in graph if cave in el}

def find_next_cave(current, graph):
    return [next(iter(cave - {current})) for cave in graph if current in cave]

def is_small_cave(c):
    return c.islower()

def add_to_deadends(path):
    global deadends
    deadends.append(path)

def add_to_paths(path):
    global paths
    paths.append(path)

def step(current, path, graph):
    path = path + [current]

    if current == "end":
        add_to_paths(path)
        return None

 #   if current in deadends:
 #       return None
    
    next_steps = find_next_cave(current, graph)
    
    if not next_steps:
#        add_to_deadends(path)
        return None
    
    if is_small_cave(current):
        graph = graph - filter_in(current, graph)

    for next_step in next_steps:
        step(next_step, path, graph)
    

def begin(graph):
    global deadends, paths
    graph = read_graph(graph)
    deadends, paths = {}, []

    step(start, [], graph)


begin(test_input)

assert '\n'.join(test_output.split('\n')) == '\n'.join(sorted(line for line in [','.join(row) for row in paths]))
assert len(paths) == 10

begin(test_input2)
assert len(paths) == 226

with open("input_day12.txt") as f:
    input_str = f.read()

begin(input_str)
print(len(paths))