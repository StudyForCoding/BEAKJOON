import sys
N = int(sys.stdin.readline())
arr1 = [1, 2]

def tile(n):
	if n == 1 or n == 2:
		return arr1[n - 1]
	for i in range(2, n):
		arr1.append((arr1[i - 1] + arr1[i - 2]) % 15746)
	return arr1[n - 1]

print(tile(N))