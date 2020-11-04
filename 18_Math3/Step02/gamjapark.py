import sys
N = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))
f.sort()
print(f[0] * f[N-1])