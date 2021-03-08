import sys
input = sys.stdin.readline
from math import sqrt
# 에리토스테네스의 체
N = int(input())
sum_list = [0] # 연속된 소수의 합 배열
a = [False,False] + [True]*(N-1)
for i in range(2,N+1):
    if a[i]:
        sum_list.append(sum_list[-1]+i)
        for j in range(2*i,N+1,i):
            a[j] = False
# 투 포인터   
l,r,cnt = 0,1,0
while l != len(sum_list)-1:
    # print(l,r)
    s = sum_list[r] - sum_list[l]
    if s >= N:
        if s == N: cnt += 1
        l += 1
    else:
        if r == len(sum_list)-1: l += 1
        else: r += 1
print(cnt)