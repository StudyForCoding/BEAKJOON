N = int(input()) #수열개수
arr = input()
arr = arr.split() 
arr= [int(i) for i in arr] #입력받은 수열배열
d = [0] * (N)#가장 긴 증가하는 부분수열 길이 
max1 = 0

for i in range(0, N):
    min1 = 0
    for j in range(0, i):
        if arr[i] > arr[j]: #앞수열보다 큰 수가 있으면
            if min1 < d[j]: #현재 인덱스요소보다 작은 수 카운트 
                min1 = d[j]
    d[i] = min1 + 1
    if max1 < d[i]:
        max1 = d[i] #d배열중 최대 값이 가장 긴 증가하는 부분수열이  
print(max1)

