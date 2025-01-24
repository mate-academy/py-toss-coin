import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    number_of_flip = 10000
    for _ in range(number_of_flip):
        count_heads = 0
        for _ in range(10):
            if random.randint(0, 1):
                count_heads += 1
        result[count_heads] = result.get(count_heads, 0) + 1

    for heads in result:
        result[heads] = round((result[heads] / number_of_flip * 100), 2)

    return result


def draw_gaussian_distribution_graph(probability: dict) -> None:
    plt.plot(probability.keys(), probability.values())

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
