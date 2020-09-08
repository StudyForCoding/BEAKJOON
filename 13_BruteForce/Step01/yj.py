from itertools import combinations

N,M = map(int, input().split())
num = list(map(int, input().split()))

max =0
for i in list(combinations(num,3)):
    total = sum(i)
    if total<=M and max<total:
        max = total
print(max)