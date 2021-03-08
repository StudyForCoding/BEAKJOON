import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
l,r,len_,s = 0,1,float('inf'),arr[0]
while l != N:
    if s >= S:
        len_ = min(len_,r-l)
        s -= arr[l]
        l += 1
    else:
        if r == N: 
            s -= arr[l]
            l += 1
        else: 
            s += arr[r]
            r += 1
print(len_ if len_ < float('inf') else 0)