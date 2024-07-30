import random

def flip_coin() -> dict:
    coin = ["head", "non-head"]
#    all_result = {}
#     out ={}
#
#     for j in range(10000):
#         result_10 = []
#         for i in range(10):
#             result_10.append(random.choice(coin))
#         all_result[j] = result_10
#     for x in all_result:
#         print(f"{x} = {all_result[x]}")
#
# # counting percentage
#     for i in range(10000):
#         count_head = 0
#         for j in range(10):
#             if all_result[i][j] == "head":
#                 print(f"{all_result[i][j]} i={i} j={j} count = {count_head}")
#                 count_head += 1
#         print(count_head)
#         out[j] = round(count_head / 10000, 2)
#     print(out)
    datas = []
    out = {}
    for index in range(10000):
        num_head = 0
        for i in range(10):
            result = random.choice(coin)
            if result == "head":
                num_head += 1
        datas.append(num_head)

    for n in range(11):
        out[n] = round(datas.count(n) / 10000, 2)
    print(out)

    return out






if __name__== "__main__":
    flip_coin()