N=int(input()) #삼각형의 크기

matrix = [] #삼각형 배열

for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(len(matrix[i])):
        if j==0: #첫 열의 요소일 때
            matrix[i][j]+= matrix[i-1][j]
        elif j==len(matrix[i])-1: #끝 열의 요소일 때
            matrix[i][j]+= matrix[i-1][j-1]
        else: #나머지 열의 요소일 때: 위의 두개 중 큰 값 선택해서 더함
            matrix[i][j]+=max(matrix[i-1][j-1], matrix[i-1][j])

print(max(matrix[N-1]))

