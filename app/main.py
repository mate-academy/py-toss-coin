import random


def flip_once() -> int:
    heads_count = 0
    for _ in range(10):
        if random.choice([0, 1]) == 1:
            heads_count += 1
    return heads_count


def flip_experiment(trials: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = flip_once()
        results[heads_count] += 1
    percentages = {k: (v / trials) * 100 for k, v in results.items()}
    return percentages


print(flip_experiment())
