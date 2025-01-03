import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            head_tail = random.randint(0, 1)
            if head_tail == 1:
                head += 1
        res[head] += 1
    return {k: v / 100 for (k, v) in res.items()}


def draw_gaussian_distribution_graph():
    plt.plot([y for y in flip_coin().values()])
    plt.show()
