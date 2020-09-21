mappp = [list(map(int, input().split())) for _ in range(9)]
pos = []
for i in range(9):
	for j in range(9):
		if mappp[i][j] == 0:
			pos.append([i, j])
enddd = False
def back_dfs(idx):
	global enddd
	if enddd:
		return 
	if idx == len(pos):
		for i in range(9):
			for j in range(9):
				print(mappp[i][j], end=" ")
			print()
		enddd = True
		return
	else:
		x = pos[idx][0]
		y = pos[idx][1]
		arr = [i for i in range(1, 10)]
		for a in range(9):
			if mappp[x][a] in arr:
				arr.remove(mappp[x][a])
			if mappp[a][y] in arr:
				arr.remove(mappp[a][y])

		start_i = (x // 3) * 3
		start_j = (y // 3) * 3
		for a in range(start_i, start_i + 3):
			for b in range(start_j, start_j  + 3):
				if mappp[a][b] in arr:
					arr.remove(mappp[a][b])
		for a in arr:
			mappp[x][y] = a
			back_dfs(idx + 1)
			mappp[x][y] = 0

back_dfs(0)