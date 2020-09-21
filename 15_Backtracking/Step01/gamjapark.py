N, M = map(int, input().split())
a = [0] * M
b = [0] * (N + 1)

def dfs(idx):
	if idx == M:
		for aa in a:
			print(aa, end=" ")
		print()
		return

	for i in range(1, N + 1):
		if b[i] == 1:
			continue
		a[idx] = i
		b[i] = 1
		dfs(idx + 1)
		b[i] = 0
dfs(0)
