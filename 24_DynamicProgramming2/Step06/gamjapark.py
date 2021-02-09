import sys
n, k = map(int, sys.stdin.readline().split())
coin=[]
for i in range(n):
	coin.append(int(sys.stdin.readline()))

result = [0 for _ in range(k + 1)]
result[0] = 1
for c in coin:
	for i in range(c, k + 1):
		result[i] += result[i-c]
	print(result)

print(result[k])