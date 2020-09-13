import sys

n = int(sys.stdin.readline())
num_list = [0 for _ in range(10001)]
for _ in range(n):
    num = int(sys.stdin.readline())
    num_list [num] += 1

for i in range(1, 10001):
    for _ in range(num_list [i]):
        print(i)