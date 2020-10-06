N=int(input()) #집의 수

matrix = [] #N개의 집에 대한 R, G, B 비용 map배열

for i in range(N):
    #각 색별 페인트 비용 map
    matrix.append(list(map(int, input().split())))
 
for i in range(1, N):
        #i번째 집을 빨강으로 칠했을 때의 최소값
        matrix[i][0] = matrix[i][0] + min(matrix[i-1][1], matrix[i-1][2])
        #i번째 집을 초록으로 칠했을 때의 최소값
        matrix[i][1] = matrix[i][1] + min(matrix[i-1][0], matrix[i-1][2])
        #i번째 집을 파랑으로 칠했을 때의 최소값
        matrix[i][2] = matrix[i][2] + min(matrix[i-1][0], matrix[i-1][1])
 
print (min(min(matrix[N-1][0], matrix[N-1][1]), matrix[N-1][2]))

