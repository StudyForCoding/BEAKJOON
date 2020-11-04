N, K=map(int, input().split())
arr=[]
result=0
for i in range(N):
    arr.append(int(input()))

for i in range(N-1, -1, -1):
    if K==0:
        break
    else:
        result+=K//arr[i]
        K=K%arr[i]

print(result)
