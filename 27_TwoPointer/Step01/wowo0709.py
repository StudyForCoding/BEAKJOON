import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
x = int(input())

l,r,cnt = 0,n-1,0
while l < r:
    tmp = arr[l] + arr[r]
    if tmp <= x:
        if tmp == x: cnt += 1
        l += 1
    else: r -= 1
print(cnt)