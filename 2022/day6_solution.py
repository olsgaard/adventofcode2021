from shared import sliding_window

examples = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
""".strip().split('\n')

example_answers = [7,5,6,10,11]
example_answers2 = [19,23,23,29,26]

def solve(x, n):
    for i, marker in enumerate(sliding_window(x, n)):
        if len(marker) == len(set(marker)):
            return i+n

for example, answer in zip(examples, example_answers):
    assert solve(example, 4) == answer, (solve(example, 4), answer)

with open("day6_input.txt") as f:
    signal = f.read().strip()

print("solution 1:", solve(signal, 4))

for example, answer in zip(examples, example_answers2):
    assert solve(example, 14) == answer, (solve(example, 14), answer)

print("solution 1:", solve(signal, 14))

