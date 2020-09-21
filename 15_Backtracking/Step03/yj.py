import sys

N, M = map(int, sys.stdin.readline().split())
visit = [False] * (N + 1)
num = [0] * M

def problem(index, N, M):
    if index== M:
        print(' '.join(map(str,num)))
        return
    for i in range(1, N + 1):
        if visit[i] :
            continue
        #visit[i] = True
        for j in range(i):
            visit[j] = True
        num[index] = i
        problem(index + 1, N, M)
        #visit[i] = False
        for j in range(i + 1):
            visit[j] = False

problem(0,N,M)
