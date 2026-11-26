"""CSMAXXXING AI Lab - Mission 8B: Three Doors (exploration vs exploitation).

Three doors pay different rewards. The agent does not know the payouts.
Run:  python three_doors_bandit.py      (Python 3, no extra packages)
Change EPSILON (0 = never explore, 1 = always explore) and compare.
"""
import random

def pull(door, rng):
    roll = rng.randint(1, 6)                 # one die roll
    if door == "A":
        return 1                             # always +1
    if door == "B":
        return 5 if roll == 6 else 0         # +5 on a six
    return 3 if roll >= 4 else 0             # C: +3 on 4, 5 or 6

def play(strategy, rounds=50, epsilon=0.1, rng=None):
    rng = rng or random.Random()
    doors = ["A", "B", "C"]
    totals = {d: 0 for d in doors}
    counts = {d: 0 for d in doors}
    reward_sum = 0
    for t in range(rounds):
        untried = [d for d in doors if counts[d] == 0]
        if untried:
            door = untried[0]                                   # try each door once
        elif strategy == "random" or (strategy == "epsilon" and rng.random() < epsilon):
            door = rng.choice(doors)                            # EXPLORE
        else:
            door = max(doors, key=lambda d: totals[d] / counts[d])  # EXPLOIT best average so far
        r = pull(door, rng)
        totals[door] += r
        counts[door] += 1
        reward_sum += r
    return reward_sum, counts

if __name__ == "__main__":
    rng = random.Random(42)
    games = 2000
    for strategy in ["greedy", "epsilon", "random"]:
        scores = [play(strategy, rng=rng)[0] for _ in range(games)]
        print(f"{strategy:>8}: average total reward over 50 rounds = {sum(scores)/games:.1f}")
    print("Best possible on average: always door C = 1.5 per round = 75 per 50 rounds")
