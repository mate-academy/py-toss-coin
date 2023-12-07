import random
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10000, num_coin_tosses: int = 10) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(num_flips):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coin_tosses))
        result[num_heads] += 1

    percentage_results = {
        key: (value / num_flips * 100) for key, value in result.items()
    }
    return percentage_results


def draw_gaussian_distribution_graph(distribution_data: dict) -> None:
    keys = list(distribution_data.keys())
    values = list(distribution_data.values())

    plt.plot(keys, values, color="blue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution")
    plt.ylim(0, 100)
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)

    draw_gaussian_distribution_graph(results)
