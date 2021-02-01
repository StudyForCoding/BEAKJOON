import sys

N = int(sys.stdin.readline())
paper = []
for i in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	paper.append(tmp)

def solution(i, j, n):
	tmp = []
	for a in range(i, i+n):
		tmp.append(paper[a][j:j+n])
	one_paper = sum(tmp, [])
	if len(set(one_paper)) == 2 and n > 1:
		new_size = n//2
		white = [0,0,0,0]
		blue = [0,0,0,0]
		white[0], blue[0] = solution(i, j, new_size)
		white[1], blue[1] = solution(i, j+new_size, new_size)
		white[2], blue[2] = solution(i+new_size, j, new_size)
		white[3], blue[3] = solution(i+new_size, j+new_size, new_size)
		return sum(white), sum(blue)
	else:
		if one_paper[0] == 0:
			return 1, 0
		else:
			return 0, 1
		
white,blue = solution(0,0,N)
print(white)
print(blue)
