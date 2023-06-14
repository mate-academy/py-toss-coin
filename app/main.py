import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flips = 0
    cases = {i: 0 for i in range(11)}
    for _ in range(10000):
        sides = []
        flips += 1
        for _ in range(10):
            case = random.choice(["Head", "Tail"])
            sides.append(case)
        cases[sides.count("Head")] += 1

    return {key: round(value / flips * 100, 2) for key, value in cases.items()}


normal_distribution = flip_coin()


plt.plot([case for case in normal_distribution],
         [value for value in normal_distribution.values()])

plt.xlabel("Heads count")
plt.ylabel("Drop percentage, %")
plt.title("Gaussian distribution")
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 101, 10))
# plt.show()  should be uncommented
