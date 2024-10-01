import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}
    for case in range(10000):
        head_count = 0
        for flip in range(10):
            if random.choice(["head", "tail"]) == "head":
                head_count += 1
        result[head_count] += 1
    result = {key: round(value / 100, 2) for key, value in result.items()}
    return result


ypoints = np.array([value for value in flip_coin().values()])
plt.plot(ypoints)
plt.ylim(0, 100)
plt.xlim(0, 10)
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.show()
