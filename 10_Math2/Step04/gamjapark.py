import math

min_ = []
max_ = []
while True:
    a = int(input())
    if a == 0:
        break
    min_.append(a)
    max_.append(2 * a)

min_num = min(min_)
max_num = max(max_)
result = [0 for _ in range(max_num + 1)]

for idx in range(min_num, max_num + 1):
    check = True
    for i in range(2, int(math.sqrt(idx)) + 1):
        if idx % i == 0:
            check = False
            break
    if check:
        result[idx] = 1

for idx in min_:
    print(sum(result[idx + 1:(2*idx + 1)]))