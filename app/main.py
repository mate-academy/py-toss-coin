import random


def flip_coin() -> dict:

    cases_count = 10000
    flip_per_case = 10
    all_cases_result = []
    for _ in range(cases_count):
        head_was_flipped = []
        for _ in range(flip_per_case):
            head_was_flipped.append(random.choice([False, True]))

        all_cases_result.append(head_was_flipped.count(True))

    result = {}
    for possible_heads in range(flip_per_case + 1):
        result[possible_heads] = all_cases_result.count(
            possible_heads) / (cases_count / 100)

    return result

# 20% FROM 10 000
# (10 000 / 100) * 20 =  X
# So if we know x, but don't know percentage(20),
# we can create next (10 000 / 100) * X =  2000
#  so 2 000 / (10 000 / 100) = x
