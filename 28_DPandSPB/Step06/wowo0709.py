import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = sys.maxsize
dpos = ['-1','+1','*2']

def dijkstra(x):
    path = [-1 for _ in range(100001)]
    hp = []
    heappush(hp,(0,x)) # 이동횟수, 위치
    while hp:
        ct,cx = heappop(hp)
        if times[cx] < ct: continue
        for dp in dpos:
            nx = eval('cx' + dp)
            if 0 <= nx <= 100000 and ct+1 < times[nx]:
                times[nx] = ct + 1
                path[nx] = cx
                heappush(hp,(ct+1,nx))
        if times[K] != INF: break
    return path

N,K = map(int,input().split())
times = [INF for _ in range(100001)] # 이동횟수
times[N] = 0
path = dijkstra(N)
toN,ans = K,[K]
while path[toN] != -1:
    toN = path[toN] # fromN
    ans.append(toN)
print(times[K])
print(*reversed(ans))


     
