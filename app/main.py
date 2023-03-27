import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> None:
    result_dict = {i: 0 for i in range(11)}
    for i in range(10000):
        head = 0
        for number in range(10):
            if random.choice(["Head", "beack"]) == "Head":
                head += 1
        result_dict[head] += 1

    for i in range(11):
        result_dict[i] /= 100
    return result_dict


array_dict = flip_coin()
array_x = []
array_y = []
for i in range(11):
    array_y.append(array_dict[i])
    array_x.append(i)
plt.plot(array_x, array_y, color="b")
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.title("Gaussian distribution")
plt.show()
