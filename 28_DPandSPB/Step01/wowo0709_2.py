import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = sys.maxsize

def dijkstra(N): # 다익스트라 알고리즘 응용
    path = [0 for _ in range(N+1)] # path[to] = from (최단경로 역추적)
    hp = []
    heappush(hp,(0,N))
    while hp:
        ct,cn = heappop(hp)
        nns = [0,0,0] # 코드 간략화
        if times[cn] < ct: continue
        if cn - 1 > 0: nns[0] = cn - 1
        if cn % 2 == 0: nns[1] = cn // 2
        if cn % 3 == 0: nns[2] = cn // 3
        for nn in nns:
            if nn > 0 and ct + 1 < times[nn]:
                times[nn] = ct + 1
                path[nn] = cn
                heappush(hp,(ct+1,nn))
    return path

N = int(input())
times = [INF for _ in range(N+1)] # N이 되는 최소 계산 횟수
times[N] = 0 # 자기 자신은 0
path = dijkstra(N)
toN,ans = 1,[1]
while path[toN] != 0:
    toN = path[toN] # fromN
    ans.append(toN)
print(times[1])
print(*ans[::-1])