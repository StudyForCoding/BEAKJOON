import sys

N = int(sys.stdin.readline())
paper = []
result = {-1:0, 0:0, 1:0}

for i in range(N):
	paper.append(list(map(int, sys.stdin.readline().split())))

def solution(i, j, n):
	c = paper[i][j]
	check = False
	for a in range(n):
		for b in range(n):
			if paper[i+a][j+b] != c:
				check = True
				break
		if check:
			break

	if check and n > 1:
		new_size = n//3
		for p in range(3):
			for q in range(3):
				solution(i + p*new_size, j + q*new_size, new_size)
		return result
	else:
		result[c] += 1

solution(0,0,N)
print(*list(result.values()),sep="\n")
