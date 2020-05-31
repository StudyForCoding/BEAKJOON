import sys
n=int(input())
arr = [int(x) for x in sys.stdin.readline().split()]
print("%d %d"%(min(arr), max(arr)))