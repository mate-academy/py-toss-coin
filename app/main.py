import numpy as np


def flip_coin(
        success_rate: float = 0.5,
        exp_count: int = 10000,
        flips: int = 10
) -> dict:
    results = np.random.binomial(flips, success_rate, exp_count)
    unique, counts = np.unique(results, return_counts=True)
    percentages = (counts / exp_count) * 100
    return {key: round(value, 2) for key, value in zip(unique, percentages)}
