import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10000

    for trial in range(num_trials):
        num_heads = 0
        for num in range(10):
            if random.random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1
    for key in results:
        results[key] = 100.0 * results[key] / num_trials
    return results
