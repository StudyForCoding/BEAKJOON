import sys
arr = [int(sys.stdin.readline().rstrip()) for i in range(9)]
print(max(arr))
print(arr.index(max(arr)) + 1)