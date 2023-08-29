import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        times = 0
        for i in range(10):
            if random.choice([True, False]):
                times += 1
        res[times] += 1
    for time in res:
        res[time] = round(res[time] / 100, 2)
    return res


plt.plot(flip_coin().keys(), flip_coin().values())
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.xticks(range(0, 11))
plt.yticks(range(0, 101, 10))
plt.show()
