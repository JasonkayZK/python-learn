nums = [11, 22, 33, 44, 55]


def judge(x):
    if x % 2 == 0:
        return True
    else:
        return False


res = list(filter(judge, nums))
print(res)
