import sys

N, M = map(int, sys.stdin.readline().split())
visit = [False] * (N + 1)
num = [0] * M

def problem(index, N, M):
    if index== M:
        print(' '.join(map(str,num)))
        return
    for i in range(1, N + 1):
        if visit[i]:
            continue
        visit[i] = True
        num[index] = i
        problem(index + 1, N, M)
        visit[i] = False

problem(0,N,M)