import sys
input = sys.stdin.readline
from bisect import bisect_left
# 시간 복잡도: O(NlogN) -> 완전 탐색 + 이분 탐색
def LIS(arr):
    BSlist = [arr[0]] # 이분 탐색에 의해 갱신될 LIS 리스트
    idxs = [0]        # 경로 역추적에 사용될 인덱스 리스트
    for n in arr[1:]:
        if BSlist[-1] < n:
            BSlist.append(n)
            idxs.append(len(BSlist)-1)
        else:
            idx = bisect_left(BSlist,n)
            BSlist[idx] = n
            idxs.append(idx)
    i = len(BSlist)
    ans = []
    for idx in range(len(idxs)-1,-1,-1):
        if idxs[idx] == i-1:
            ans.append(arr[idx])
            i -= 1
    return ans[::-1]

N = int(input())
A = list(map(int,input().split()))
ans = LIS(A)
print(len(ans))
print(*ans)