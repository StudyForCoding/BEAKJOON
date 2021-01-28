import sys
input = sys.stdin.readline

BLACK = 1
WHITE = 0
answer = []

def quadTree(n,matrix):
    global answer
    if n == 1:
        if matrix[0][0] == BLACK:  answer.append('1')
        else:  answer.append('0')
        return

    cnt_black,cnt_white = 0,0

    for row in matrix:
        cnt_black += row.count(BLACK)
        cnt_white += (n - cnt_black)

    if cnt_black == n**2:  answer.append('1')
    elif cnt_white == n**2:  answer.append('0')
    else:  
        answer.append('(')
        quadTree(n//2,[row[:n//2] for row in matrix[:n//2]])
        quadTree(n//2,[row[n//2:] for row in matrix[:n//2]])
        quadTree(n//2,[row[:n//2] for row in matrix[n//2:]])
        quadTree(n//2,[row[n//2:] for row in matrix[n//2:]])
        answer.append(')')


n = int(input())
matrix = [[int(x) for x in list(input().rstrip())] for _ in range(n)]
quadTree(n,matrix)
print(''.join(answer))