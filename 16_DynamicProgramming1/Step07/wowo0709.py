n = int(input())
step = [0]*(n+2);score = [0]*(n+2)
for i in range(n):
    step[i] = int(input())
score[0] = step[0];score[1] = step[0] + step[1]
score[2] = max(step[0]+step[2],step[1]+step[2])
for i in range(3,n):
    score[i] = max(score[i-3]+step[i-1]+step[i],score[i-2]+step[i])
print(score[n-1])