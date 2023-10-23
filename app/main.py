import random
import matplotlib.pyplot as ptl


def flip_coin() -> dict:
    coins_sides = ["head", "tail"]
    heads_count = {}
    for _ in range(10000):
        head = 0
        for i in range(10):
            if random.choice(coins_sides) == "head":
                head += 1
        if head in heads_count.keys():
            heads_count[head] += 1
        else:
            heads_count[head] = 1
    sorted_heads_count = {key: round(heads_count[key] / 10000 * 100, 2)
                          for key in sorted(heads_count)}
    return sorted_heads_count


def draw_gaussian_distribution_graph() -> None:
    x_point = []
    y_point = []
    for key, value in flip_coin().items():
        x_point.append(key)
        y_point.append(value)
    ptl.xlim(0, 10)
    ptl.ylim(0, 100)
    ptl.xticks(range(11))
    ptl.yticks(range(0, 101, 10))
    ptl.plot(x_point, y_point)
    ptl.xlabel("Heads count")
    ptl.ylabel("Percentage %")
    ptl.title("Gaussian distribution")
    ptl.show()
