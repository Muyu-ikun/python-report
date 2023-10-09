import math

def nearest_sq(n):
    # 如果n是完全平方数，则直接返回n
    if int(math.sqrt(n))**2 == n:
        return n
    # 否则，找到n的平方根
    root = int(math.sqrt(n))
    # 找到比n大的最小平方数
    next_sq = (root+1)**2
    # 找到比n小的最大平方数
    prev_sq = (root)**2
    # 判断哪个更接近n
    if n - prev_sq < next_sq - n:
        return prev_sq
    else:
        return next_sq


print(nearest_sq(111)) # 121
print(nearest_sq(144)) # 144
print(nearest_sq(81)) # 81
print(nearest_sq(10)) # 9
print(nearest_sq(25)) # 25
print(nearest_sq(30)) # 25

