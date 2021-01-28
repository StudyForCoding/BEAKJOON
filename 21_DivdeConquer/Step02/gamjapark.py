import sys

N = int(sys.stdin.readline())
paper = []
for i in range(N):
	tmp = list(map(int,sys.stdin.readline().split()[0]))
	paper.append(tmp)
result = []

def solution(i, j, n):
	tmp = []
	for a in range(i, i+n):
		tmp.append(paper[a][j:j+n])
	one_paper = sum(tmp, [])
	if len(set(one_paper)) == 2 and n > 1:
		new_size = n//2
		white = [0,0,0,0]
		blue = [0,0,0,0]
		result.append("(")
		solution(i, j, new_size)
		solution(i, j+new_size, new_size)
		solution(i+new_size, j, new_size)
		solution(i+new_size, j+new_size, new_size)
		result.append(")")
	else:
		if one_paper[0] == 0:
			result.append("0")
		else:
			result.append("1")
		
solution(0,0,N)
print(*result,sep="")
