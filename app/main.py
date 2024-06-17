import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}

    for _ in range(10000):
        head = 0
        for __ in range(10):
            if random.randint(0, 1) == 1:
                head += 1
        result[head] += 0.01

    # coin_sides = ["Heads", "Tails"]
    # tosses_of_ten_times = {}
    # for i in range(10000):
    #     times_in_tosses = {}
    #     for time_of_toss in range(10):
    #         toss = random.choice(coin_sides)
    #         times_in_tosses[time_of_toss] = toss
    #     tosses_of_ten_times[i] = times_in_tosses
    # statistics_of_ten_times = {i: 0 for i in range(10)}
    # heads_in_zero_time = 0
    # for toss in tosses_of_ten_times.values():
    #     if toss[0] == "Heads":
    #         heads_in_zero_time += 1
    #
    # for key in statistics_of_ten_times:
    #     heads_in_zero_time = 0
    #     for toss in tosses_of_ten_times.values():
    #         if toss[key] == "Heads":
    #             heads_in_zero_time += 1
    #     statistics_of_ten_times[key] = round(
    #         100 / len(tosses_of_ten_times) * heads_in_zero_time, 2
    #     )
    # return statistics_of_ten_times
    return result

if __name__ == "__main__":
    print(flip_coin())