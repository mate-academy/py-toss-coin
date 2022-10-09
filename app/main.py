from random import randint
from matplotlib import pyplot as plt


def chance_of_zero_from_10() -> int:
    count_zeros = 0
    for _ in range(10):
        if randint(0, 1) == 0:
            count_zeros += 1
    return count_zeros


def flip_coin() -> dict:
    heads_dropped: dict = {}
    for _ in range(10_000):
        count_zeros = chance_of_zero_from_10()
        if count_zeros in heads_dropped.keys():
            heads_dropped[count_zeros] += 1
        else:
            heads_dropped[count_zeros] = 1
    return {key: value / 100 for key, value in
            dict(sorted(heads_dropped.items())).items()}


flip_coin_result = flip_coin()
dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
plt.axis([0, 10, 0, 100])
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")

xs = []
ys = []
for i in range(10):
    xs.append(i + 1)
    ys.append(flip_coin_result[i])

plt.plot(xs, ys, color="blue", linestyle="solid")
plt.grid(True)
fig.savefig("gaussian.png")
