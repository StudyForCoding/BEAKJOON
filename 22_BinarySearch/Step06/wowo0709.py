'''
1. low=1(최소), high=N**2(최대), mid=(low+high)//2로 선언. 이 때 mid가 구하고자 하는 수를 나타냄.
2. 각 행을 for문에서 돌면서 mid보다 큰 수의 개수(cnt)를 조사한다. 
2-1. mid보다 커지기 시작하는 수의 인덱스(bigger_idx)를 구한다. 
2-2. bigger_idx를 기준으로 해당 행에서 mid보다 큰 수의 개수를 구하고, cnt에 더한다. 
3. cnt가 너무 작다면 high=mid-1로 mid를 줄이고, cnt가 너무 크다면 low=mid+1로 mid를 키운다. 
4. low <= high인 동안 1~3 과정을 반복한다. 
*** 작은 수의 개수를 기준으로 할 수도 있다. 다만 작은 수를 기준으로 하려면, 값이 같을 경우를 고려해야 한다.***
'''
N = int(input())
k = int(input())

low,high,ans = 1,N**2,0
while low <= high:
    mid = (low+high) // 2
    cnt = 0 # mid 보다 큰 수의 개수를 센다.
    for n in range(1,N+1):
        bigger_idx = mid//n + 1 # mid보다 커지기 시작하는 수의 인덱스 값
        cnt += (N-bigger_idx+1) if bigger_idx<=N else cnt

    if cnt <= N**2-k: # 큰 수가 적거나 같다면 수를 줄인다. 
        high = mid-1
        ans = mid
    else:             # 큰 수가 많다면 수를 키운다. 
        low = mid+1

print(ans)