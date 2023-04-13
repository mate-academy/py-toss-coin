import random
import matplotlib.pyplot as plt

def flip_coin() -> dict:
    stats = {key: 0 for key in range(0, 11)}
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            if random.choice((1, 2)) == 2:
                count += 1
        stats[count] += 1
    stats = {key: round((value / 10_000) * 100, 2) for key, value in stats.items()}
    return stats


if __name__ == '__main__':
    data = flip_coin()

    plt.plot(data.keys(), data.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
