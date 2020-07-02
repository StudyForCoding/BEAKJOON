N = int(input())

result = 0
for i in range(1,N):
    num =list(map(int,str(i)))
    sum = 0
    for j in num:
        sum+=j
    if sum +i == N:
        result = i
        break
print(result)