import random
from pprint import pprint


def flip_coin() -> dict[int: float]:
    heads_all_counts = []
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice(['heads', 'tails']) == 'heads':
                heads_count += 1
        heads_all_counts.append(heads_count)
    return {k: heads_all_counts.count(k) / len(heads_all_counts) for k in range(11)}




if __name__ == '__main__':
    cache = set()

    for _ in range(20):
        coins = flip_coin()
        pprint(coins)
        cache.add(tuple(result for result in coins.values()))
    ## pprint(cache)