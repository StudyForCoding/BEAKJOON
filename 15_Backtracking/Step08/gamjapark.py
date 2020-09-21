from itertools import combinations
import sys
N = int(input())
mappp = [list(map(int, input().split())) for _ in range(N)]
team = [i for i in range(N)]
arr = list(combinations(team, N//2))
answer = sys.maxsize

for i in range(len(arr) - 1):
	s, l = 0, 0
	for j in range(i + 1, len(arr)):
		ttt = set(arr[j] + arr[i])
		if len(ttt) != N:
			continue
		else:
			aaa = list(combinations(arr[i], 2))
			bbb = list(combinations(arr[j], 2))
			for a in range(len(aaa)):
				(x, y) = aaa[a]
				s += (mappp[x][y] + mappp[y][x])

			for b in range(len(bbb)):
				(x, y) = aaa[a]
				l += (mappp[x][y] + mappp[y][x])
			answer = min(answer, abs(s-l))
print(answer)