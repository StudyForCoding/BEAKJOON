#1135ms
import sys
N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

minNum, maxNum = 1, k

# 2*1 ~ 2*10  20 > 2*n -> min(20//2, N)

while minNum <= maxNum:
	mid = (minNum + maxNum)//2
	count = 0
	for i in range(1, N + 1):
		count += min(N, mid//i)
		if count >= k:
			answer = mid
			maxNum = mid - 1
			break
	if count < k:
		minNum = mid + 1
print(answer)