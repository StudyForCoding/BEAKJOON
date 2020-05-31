import sys
n, x = map(int, sys.stdin.readline().split())
for a in sys.stdin.readline().split():
    if int(a) < x:
        print(a, end=" ")