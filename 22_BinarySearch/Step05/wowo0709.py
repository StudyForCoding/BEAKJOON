'''
1. 최소거리(low)와 최대거리(high)의 평균값(mid)으로 거리 설정.
2. x좌표들을 for문을 돌면서, 거리가 mid 이상이 되면 cnt+=1 하고 기준이 되는 좌표(criteria)를 리셋.
3. 구한 cnt와 C를 비교. cnt >= C 이면 low=mid+1로 거리를 늘리고, cnt<C 이면 high=mid-1로 거리를 줄임.
4. 1~3 과정을 low<=high 인 동안 반복.
'''
N,C = map(int,input().split())
x = []
for _ in range(N):
    x.append(int(input()))
x.sort()

low,high,ans = 1,x[-1]-x[0],0
while low <= high:
    mid = (low+high) // 2
    criteria = x[0]
    cnt = 1
    for i in range(N):
        if x[i]-criteria >= mid:
            cnt += 1
            criteria = x[i]

    if cnt >= C:
        low = mid+1
        ans = mid
    else:
        high = mid-1

print(ans)