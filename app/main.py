import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    statistics = {}

    for test in range(10000):
        heads_count = 0

        for attempt in range(10):
            if random.choice(["tails", "heads"]) == "heads":
                heads_count += 1

        if heads_count not in statistics:
            statistics[heads_count] = 1 / 10000 * 100
        else:
            statistics[heads_count] += 1 / 10000 * 100

    return {key: round(statistics[key], 2) for key in range(11)}


# ----------------Graph creation----------------


flip_stats = flip_coin()

heads_number = [i for i in range(11)]
probability = [value for value in flip_stats.values()]

plt.plot(heads_number, probability)
plt.xticks(heads_number, size=8)
plt.ylabel("Drop percentage, %")
plt.xlabel("Heads count")
plt.grid()

plt.show()
