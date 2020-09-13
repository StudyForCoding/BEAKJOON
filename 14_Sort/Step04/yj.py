import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num =[]

for i in range(N):
    num.append(int(input().rstrip()))

num.sort()
count = Counter(num)
common = count.most_common(n=2)
print(round(sum(num)/len(num)))
print(num[len(num)//2])
if len(common)>=2:
    if common[0][1]==common[1][1]:
        print(common[1][0])
    else:
        print(common[0][0])
else:
    print(common[0][0])
print(max(num)-min(num))   