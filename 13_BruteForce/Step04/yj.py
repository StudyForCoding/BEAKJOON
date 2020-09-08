N,M = map(int, input().split())
chess1 = [['W','B']*4,['B','W']*4]*4
chess2 = [['B','W']*4,['W','B']*4]*4

chess=[]

for n in range(N):
    chess.append(list(input()))

num=[]
for x in range(0, M-7):
    for y in range(0,N-7):
        num1 =0
        num2 =0
        for i in range(8):
            for j in range(8):
                if chess[y+i][x+j] != chess1[i][j]:
                    num1+=1
                if chess[y+i][x+j] != chess2[i][j]:
                    num2+=1
        num.append(min(num1,num2))
print(min(num))
                