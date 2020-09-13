import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for m in range(n)]
num.sort()

for nu in num:
    print(nu)