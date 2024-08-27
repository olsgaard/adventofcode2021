from itertools import cycle

hands = "RPS"
scores = {hand:i for i, hand in enumerate(hands, 1)}
codes = {k:v for k, v in zip("ABCXYZ", cycle("RPS"))}
coded_score = {k:scores[v] for k,v in codes.items()}

decision = {"RP": 6, "RR": 3, "RS": 0, 
            "PS": 6, "PP": 3, "PR": 0,
            "SR": 6, "SS": 3, "SP": 0}

example_strategy = """
A Y
B X
C Z
""".strip()

def score_strategy(x: str):
    total = 0
    for line in x.split("\n"):
        opponent, you = line.split()
        score = decision[f"{codes[opponent]}{codes[you]}"] + coded_score[you]
        total += score
    return total

assert score_strategy(example_strategy) == 15

with open("day2_input.txt") as f:
    strategy = f.read().strip()
    print("Part 1:", score_strategy(strategy))

xyz = {"X": 0, "Y": 3, "Z":6}
def score_strategy2(x: str):
    total = 0
    for line in x.split("\n"):
        opponent, you = line.split()
        target_score = xyz[you]
        opponent = codes[opponent]
        your_hand = next(hands[-1] for hands, value in decision.items() if hands.startswith(opponent) and (value == target_score))
        total += target_score + scores[your_hand]
    return total

assert score_strategy2(example_strategy) == 12, score_strategy2(example_strategy)

with open("day2_input.txt") as f:
    strategy = f.read().strip()
    print("Part 1:", score_strategy2(strategy))