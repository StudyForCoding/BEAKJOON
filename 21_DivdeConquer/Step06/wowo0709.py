import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
A = [[int(x) for x in input().rstrip().split()] for _ in range(n)]
m, k = map(int,input().rstrip().split())
B = [[int(x) for x in input().rstrip().split()] for _ in range(m)]
# 행렬 곱
C = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        for z in range(k):
            C[x][z] += A[x][y] * B[y][z]
# 출력 양식                
for row in C:
    for e in row:
        print(e,end = ' ')
    print()