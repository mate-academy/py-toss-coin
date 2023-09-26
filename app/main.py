import numpy as np
from scipy.stats import binom


def flip_coin() -> None:
    num_trials = 10000  # Кількість випробувань
    num_coin_flips = 10  # Кількість підкидань монети

    # Ймовірність випадіння голови у одному підкиданні монети (50%)
    p_heads = 0.5

    # Згенерувати випадкові результати для num_trials випробувань
    results = np.random.binomial(num_coin_flips, p_heads, num_trials)

    # Підрахувати кількість випадків для кожної можливої кількості голів
    counts = np.bincount(results)

    # Розрахувати відсоток для кожної кількості голів
    total_trials = float(num_trials)
    probabilities = {i: (count / total_trials) * 100 for i, count in enumerate(counts)}

    return probabilities

# Вивести результати


probabilities = flip_coin()
print(probabilities)
