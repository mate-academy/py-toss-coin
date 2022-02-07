import matplotlib.pyplot as plt
import random


def flip_coin(cases: int) -> dict:
    template = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(cases):
        temp_result = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                temp_result += 1
        template[temp_result] += 1
    result = {x: int(template[x] / cases * 100) for x in template}
    return result


def draw_gaussian_distribution_graph(data: dict):
    x = list(data.keys())
    y = list(data.values())
    plt.axis([0, 10, 0, 100])
    plt.plot(x, y)
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.show()


if __name__ == '__main__':
    draw_gaussian_distribution_graph(flip_coin(10000))
