import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

circle = deque()
result = []

for i in range(1, N + 1):
	circle.append(i)

while circle:
	for k in range(K - 1):
		circle.append(circle.popleft())
	result.append(circle.popleft())
print("<", end="")
for i in range(N):
	if i != N - 1:
		print(str(result[i]) + ",", end=" ")
		continue
	print(result[i], end="")

print(">")
