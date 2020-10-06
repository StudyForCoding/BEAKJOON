import sys
T = int(sys.stdin.readline())

def fibonacci(n):
	arr1 = [[1, 0],[0, 1]]
	if n == 0 or n == 1:
		return arr1[n]
	for i in range(2, n + 1):
		a = arr1[i - 1][0] + arr1[i - 2][0]
		b = arr1[i - 1][1] + arr1[i - 2][1]
		arr1.append([a, b])
	return arr1[n]

for a in range(T):
	num = int(sys.stdin.readline())
	answer = fibonacci(num)
	print(answer[0], answer[1])