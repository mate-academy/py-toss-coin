import random
from collections import defaultdict

def flip_coin() -> dict:
    trials = 10000
    flips_per_trial = 10
    results = defaultdict(int)

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        results[heads] += 1

    for heads in results:
        results[heads] = (results[heads] / trials) * 100

    return dict(results)

print(flip_coin())
