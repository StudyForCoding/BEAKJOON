import sys
T = int(sys.stdin.readline())

def spiral(n):
	arr1 = [1, 1, 1, 2, 2]
	if n >= 0 and n <= 4:
		return arr1[n]
	for i in range(5, n + 1):
		arr1.append(arr1[i - 1] + arr1[i - 5])
	return arr1[n]

for a in range(T):
	num = int(sys.stdin.readline())
	print(spiral(num - 1))