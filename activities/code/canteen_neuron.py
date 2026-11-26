"""CSMAXXXING AI Lab - Mission 7: The Canteen Neuron (Connectionist AI).

Run:  python canteen_neuron.py          (Python 3, no extra packages)
Then edit WEIGHTS or THRESHOLD below, predict what changes, and run again.
"""
WEIGHTS = {"friend": 2, "rain": -3, "hungry": 2}   # try rain = -1
THRESHOLD = 2                                      # go if total >= THRESHOLD

CASES = {  # case: (friend, rain, hungry)
    "A": (1, 0, 0), "B": (1, 1, 0), "C": (0, 1, 1), "D": (0, 0, 1), "E": (1, 1, 1),
}

def neuron(friend, rain, hungry):
    total = friend * WEIGHTS["friend"] + rain * WEIGHTS["rain"] + hungry * WEIGHTS["hungry"]
    return total, ("GO" if total >= THRESHOLD else "stay")

if __name__ == "__main__":
    print(f"weights={WEIGHTS}  threshold={THRESHOLD}")
    print("case friend rain hungry | total decision")
    for name, (f, r, h) in CASES.items():
        total, decision = neuron(f, r, h)
        print(f"  {name}    {f}     {r}     {h}    | {total:>4}  {decision}")
