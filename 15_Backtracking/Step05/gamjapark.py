import sys
N = int(sys.stdin.readline())
a = [0] * N

answer = 0
def back_dfs(idx):
	if idx == N:
		global answer
		answer += 1
		return
	else:
		for j in range(N):
			a[idx] = j
			for i in range(idx):
				if (a[i] == a[idx]) or (idx - i == abs(a[idx] - a[i])):
					break
			else:
				back_dfs(idx + 1)

back_dfs(0)
print(answer)
