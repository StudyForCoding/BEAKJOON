from itertools import combinations
import sys
N = int(input())
mappp = [list(map(int, input().split())) for _ in range(N)]
team = [i for i in range(N)]
arr = list(combinations(team, N//2))
answer = sys.maxsize

for i in range(len(arr) - 1):
	s, l = 0, 0
	aaa = list(combinations(arr[i], 2))
	bbb = list(combinations(set(team) - set(arr[i]), 2))
	for a in range(len(aaa)):
		(x, y) = aaa[a]
		s += (mappp[x][y] + mappp[y][x])

	for b in range(len(bbb)):
		(x, y) = bbb[b]
		l += (mappp[x][y] + mappp[y][x])
	answer = min(answer, abs(s-l))
print(answer)