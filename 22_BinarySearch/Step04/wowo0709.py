import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))
low,high,h = 0,max(trees),0

while low<=high:
    mid = (low+high) // 2
    myTree = sum(map(lambda t: t-mid if t-mid>0 else 0,trees))
    if myTree >= M:  
        h = mid
        low = mid+1
    else:  
        high = mid-1
