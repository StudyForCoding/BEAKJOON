import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
wished_idx = list(map(int,input().split()))

deq = deque(range(1,n+1))
cnt = 0

for idx in wished_idx:
    for i in range(len(deq)):
        if deq[i] == idx:
            if i == 0:
                break
            elif i <= len(deq)/2:
                deq.rotate(-i)
                cnt += i
            else:
                deq.rotate(len(deq)-i)
                cnt += (len(deq) - i)
            break
    deq.popleft()  

print(cnt)