import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    cmd = input().split()
    X = cmd[-1]
    cmd = cmd[0]

    if cmd == 'push_front':
        deq.appendleft(X)
    elif cmd == 'push_back':
        deq.append(X)
    elif cmd == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)