import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())))

l,r,st = 0,N-1,float('inf')
while l < r:
    tmp = arr[l] + arr[r]
    if abs(tmp) < st:
        st = abs(tmp)
        ans = [arr[l],arr[r]]
    if arr[l] <= 0 and 0 <= arr[r]:
        if abs(arr[l]) < abs(arr[r]): r -= 1
        else: l += 1
    elif arr[l] <= 0 and arr[r] <= 0: 
        l += 1
    else:
        r -= 1
print(*ans)