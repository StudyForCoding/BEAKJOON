import sys
input = sys.stdin.readline

BLUE = 1
WHITE = 0
blue,white = 0,0

def make_colored_paper(n,matrix):
    global blue,white
    if n == 1:
        if matrix[0][0] == BLUE:  blue += 1
        else:  white += 1
        return

    cnt_blue,cnt_white = 0,0

    for row in matrix:
        cnt_blue += row.count(BLUE)
        cnt_white += (n - cnt_blue)

    if cnt_blue == n**2:  blue += 1
    elif cnt_white == n**2:  white += 1
    else:  
        make_colored_paper(n//2,[row[:n//2] for row in matrix[:n//2]])
        make_colored_paper(n//2,[row[n//2:] for row in matrix[:n//2]])
        make_colored_paper(n//2,[row[:n//2] for row in matrix[n//2:]])
        make_colored_paper(n//2,[row[n//2:] for row in matrix[n//2:]])


n = int(input())
matrix = [[int(x) for x in input().rstrip().split()] for _ in range(n)]
make_colored_paper(n,matrix)
print(white,blue,sep='\n')