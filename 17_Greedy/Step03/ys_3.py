N=int(input())
arr=[]
arr=list(map(int, input().split()))
result=0

#인출하는 시간이 짧은 사람 순으로 정렬
arr.sort()
#합 계산
for i in range(N):
    for j in range(i+1):
        result+=arr[j]

print(result)
