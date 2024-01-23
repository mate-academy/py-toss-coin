import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    def dice_rolls(cnt: int) -> list[int]:
        return [random.randint(0, 1) for _ in range(cnt)].count(1)

    cases = 10000
    sequence = 10

    result = {i: 0 for i in range(11)}
    for _ in range(cases):
        result[dice_rolls(sequence)] += 1
    result = {idx: el * 100 / cases for idx, el in result.items()}
    return result


def draw_gaussian_distribution_graph(res: dict) -> None:
    x, y = list(res.keys()), list(res.values())

    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()


res = flip_coin()
draw_gaussian_distribution_graph(res)
