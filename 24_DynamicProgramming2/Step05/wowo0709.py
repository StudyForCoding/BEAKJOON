# 참고 자료: https://source-sc.tistory.com/3
import sys
input = sys.stdin.readline
# now: 현재 올라가 있는 추들의 무게의 차
# left(right): 왼쪽(오른쪽)에 올라가 있는 추들의 무게
# new = 현재 사용할 추의 순번
def scale(now,left,right):
    new = abs(left-right)
    if new not in dp:  dp.append(new)
    if now >= sinker_n:  return 0
    if mark[now][new] == 0:
        # 저울의 왼쪽에 놓는 경우
        scale(now+1,left+sinkers[now],right)
        # 저울의 오른쪽에 놓는 경우
        scale(now+1,left,right+sinkers[now])
        # 저울에 아예 놓지 않는 경우
        scale(now+1,left,right)

        mark[now][new] = 1

sinker_n = int(input())
sinkers = list(map(int,input().split()))
marble_n = int(input())
marbles = list(map(int,input().split()))
dp = []
mark = [[0]*15001 for i in range(sinker_n+1)]

scale(0,0,0)
for marble in marbles:
    if marble in dp:
        print('Y',end=' ')
    else:
        print('N',end=' ')