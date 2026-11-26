"""CSMAXXXING AI Lab - Mission 8C: Diamond Hunt (Q-learning in a tiny grid world).

An original, simplified 'mining' world inspired by the Minecraft diamond challenge:
  S = start, D = diamond (+10, ends episode), L = lava (-10, ends episode),
  every other step costs -1 (so shorter paths are better).
Run:  python diamond_hunt_qlearning.py  (Python 3, no extra packages)
"""
import random

GRID = [
    "S...L",
    ".L...",
    "...L.",
    ".L...",
    "...LD",
]
ACTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
ARROWS = {"up": "^", "down": "v", "left": "<", "right": ">"}
N = len(GRID)

def step(state, action):
    r, c = state
    dr, dc = ACTIONS[action]
    nr, nc = min(max(r + dr, 0), N - 1), min(max(c + dc, 0), N - 1)
    cell = GRID[nr][nc]
    if cell == "D":
        return (nr, nc), 10, True
    if cell == "L":
        return (nr, nc), -10, True
    return (nr, nc), -1, False

def train(episodes=300, alpha=0.5, gamma=0.9, epsilon=0.1, seed=1):
    rng = random.Random(seed)
    Q = {((r, c), a): 0.0 for r in range(N) for c in range(N) for a in ACTIONS}
    history = []
    for ep in range(episodes):
        state, total, done, steps = (0, 0), 0, False, 0
        while not done and steps < 100:
            if rng.random() < epsilon:
                action = rng.choice(list(ACTIONS))                      # explore
            else:
                best = max(Q[(state, a)] for a in ACTIONS)
                action = rng.choice([a for a in ACTIONS if Q[(state, a)] == best])  # exploit
            nxt, reward, done = step(state, action)
            target = reward if done else reward + gamma * max(Q[(nxt, a)] for a in ACTIONS)
            Q[(state, action)] += alpha * (target - Q[(state, action)])   # the Q-learning update
            state, total, steps = nxt, total + reward, steps + 1
        history.append(total)
    return Q, history

def greedy_path(Q):
    state, path = (0, 0), [(0, 0)]
    for _ in range(30):
        action = max(ACTIONS, key=lambda a: Q[(state, a)])
        state, _, done = step(state, action)
        path.append(state)
        if done:
            break
    return path

def policy_map(Q):
    rows = []
    for r in range(N):
        row = ""
        for c in range(N):
            if GRID[r][c] in "LD":
                row += GRID[r][c]
            else:
                row += ARROWS[max(ACTIONS, key=lambda a: Q[((r, c), a)])]
        rows.append(row)
    return rows

if __name__ == "__main__":
    Q, history = train()
    print("Average reward, first 20 episodes:", sum(history[:20]) / 20)
    print("Average reward, last 20 episodes: ", sum(history[-20:]) / 20)
    print("Learned policy (arrows = best action):")
    for row in policy_map(Q):
        print("   ", " ".join(row))
    print("Greedy path:", greedy_path(Q), "steps:", len(greedy_path(Q)) - 1)
