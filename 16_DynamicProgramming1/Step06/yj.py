import sys
N=int(sys.stdin.readline())
num=[]
for _ in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))
result = []
for n in range(1,N+1):
    result.append([0]*n)
result[0][0]=num[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j ==0:
            result[i][j] =result[i-1][j] + num[i][j]
        elif j==i:
            result[i][j] = result[i - 1][j-1] + num[i][j]
        else:
            result[i][j] = max(result[i-1][j] + num[i][j],result[i - 1][j-1] + num[i][j])
print(max(result[N-1]))