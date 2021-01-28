'''
1. 주어진 거듭제곱의 횟수를 이진수로 변환한다.
2. 주어진 이진수에 맞춰 행렬의 거듭제곱들을 구한다. 
3. 구한 행렬의 거듭 제곱들을 서로 곱한다. 
Ex) 행렬 A를 10번 곱한다면, 
1. 10 = 1010
2. 1010에 맞춰 A^8과 A^2를 구한다. 
3. A*10 = A^8 * A^2
'''
import sys
input = sys.stdin.readline

def MatMul(matrix1,matrix2): # 행렬곱
    res_mat = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                res_mat[x][z] += matrix1[x][y] * matrix2[y][z]
    
    for i in range(N):
        for j in range(N):
            res_mat[i][j] %= 1000
                
    return res_mat
    
    
N, b = map(int, input().rstrip().split())
A = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
# 1단계
b = bin(b)[2:]

identity_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)] #단위 행렬, 단위 행렬 x 행렬 = 행렬
answer = identity_matrix
for i in range(len(b)):
    # 2단계
    if b[-i-1] == '1':
        tmp_mul = A
        while i != 0:
            tmp_mul = MatMul(tmp_mul, tmp_mul)
            i -= 1
        # 3단계
        answer = MatMul(answer, tmp_mul)

for row in answer:
    print(*row)