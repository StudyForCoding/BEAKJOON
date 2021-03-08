import sys
input = sys.stdin.readline
## meet in the middle 알고리즘: 2^n 의 탐색시간을 반으로 쪼개 2^(n/2)로 줄인다.
# 백준 1450. 냅색문제
# 1. 무게 리스트를 반으로 쪼개 (완전탐색으로) 각각의 합 리스트를 구한다. 
# 2. 둘 중 하나의 합 리스트를 정렬한다. 
# 3. 이분탐색으로 정렬된 합 리스트의 upper_bound(또는 lower_bound)를 구한다. 
def upper_bound(low,high,key):
    while low < high:
        mid = (low+high) // 2
        if sumlist2[mid] <= key: low = mid + 1
        else: high = mid
    return high
# main
N,C = map(int,input().split())
ws = list(map(int,input().split()))
ws1,ws2 = ws[:N//2+1],ws[N//2+1:]
sumlist1,sumlist2 = [0],[0]
for i in range(len(ws1)):
    try:
        tmp = []
        for s in sumlist1: tmp.append(s+ws1[i])
        sumlist1 += tmp
        tmp.clear()
        for s in sumlist2: tmp.append(s+ws2[i])
        sumlist2 += tmp
    except:
        continue

sumlist2.sort()
ans = 0
for s in sumlist1: 
    if s <= C: ans += upper_bound(0,len(sumlist2),C-s)
print(ans)