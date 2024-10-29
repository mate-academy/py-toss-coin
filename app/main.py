import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for _ in range(10000):
        heads = 0
        for _ in range(0, 10):
            if random.choice(("heads", "tails")) == "heads":
                heads += 1
        flip_result[heads] += 1

    return {
        kay: round(value / 10000 * 100, 2)
        for kay, value in flip_result.items()
    }


x_point = list(flip_coin().values())
y_point = list(flip_coin().keys())

plt.xlim(0, 10)
plt.ylim(0, 100)
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.plot(y_point, x_point)
plt.show()
