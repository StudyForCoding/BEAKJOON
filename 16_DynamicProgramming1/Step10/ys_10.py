N = int(input())
arr = [0]
max1 = [0]*(N+1)
for i in range(1, N+1):
    arr.append(int(input())) #와인 양 배열
    if i < 3:
        max1[i] = sum(arr) #N=1, 2일땐 다 마시면 됨
    else:
        num = []
        num.append(max1[i-3]+arr[i-1]+arr[i])
        num.append(max1[i-2]+arr[i])
        num.append(max1[i-1])
        max1[i] = max(num) #세가지 경우 중 최대값 찾기
print(max1[-1]) 
