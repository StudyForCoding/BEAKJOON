import sys
N = int(sys.stdin.readline())

# append 보다 조금 빠름
arr= [0] * 10001
for i in range(N):
	num = int(sys.stdin.readline())
	arr[num] += 1

j = 1
while j < 10001:
	for i in range(arr[j]):
		print(j)
	j += 1