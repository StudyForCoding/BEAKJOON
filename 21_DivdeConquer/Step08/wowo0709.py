'''
피보나치의 수열을 분할 정복으로 빨리 풀려면 행렬의 거듭제곱을 이용하면 된다. 
[[Fn+1,Fn],[Fn,Fn-1]] = [[F2,F1],[F1,F0]]^n = [[1,1],[1,0]]^n
'''
import sys
input = sys.stdin.readline

div = int(1e9+7)
    
def find_power(matrix, power): # 행렬곱을 분할 정복으로 나누기
    if power == 1:
        return matrix
    
    if power % 2 == 0:
        tmp_mat = find_power(matrix,power//2)
        return MatMul(tmp_mat,tmp_mat)
    else:
        tmp_mat = find_power(matrix,power-1)
        return MatMul(tmp_mat,matrix)

def MatMul(matrix1,matrix2): # 행렬곱 계산
    # [[0]*N]*N 로 하면 리스트가 공유되서 다른 결과가 나옴
    res_mat = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                res_mat[x][z] += matrix1[x][y] * matrix2[y][z]

    for x in range(N):
        for y in range(N):
            res_mat[x][y] %= div

    return res_mat
                

n = int(input())
fibonacci_mat = [[1,1],[1,0]]
N = len(fibonacci_mat)
answer = find_power(fibonacci_mat,n)

print(answer[0][1]%div)