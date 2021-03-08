import sys
N, C = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

A = weights[0:N//2]
B = weights[N//2:N]

aSum, bSum = [], []

def sum_weight(arr, arrSum, l, w):
	if l == len(arr):
		arrSum.append(w)
		return arrSum
	sum_weight(arr, arrSum, l + 1, w)
	sum_weight(arr, arrSum, l + 1, w + arr[l])

sum_weight(A, aSum, 0, 0)
sum_weight(B, bSum, 0, 0)
bSum.sort()

# key 값이 없으면 key값보다 큰 가장 작은 정수 값을 찾는 것
def lower_bound(start, end, key):
	while start < end:
		mid = (start + end) // 2
		if bSum[mid] <= key:
			start = mid + 1
		else:
			end = mid
	return end

result = 0
bSum_len = len(bSum)
for i in aSum:
	if i <= C:
		result += lower_bound(0, bSum_len, C - i)
print(result)