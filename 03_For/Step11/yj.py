import sys
N, X = map(int, sys.stdin.readline().split())
nums = map(int, sys.stdin.readline().split())
for num in nums:    
    if num <X: print(num,end = ' ')