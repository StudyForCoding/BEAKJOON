import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
answerlist = []

deq = deque(range(1,n+1))

while deq:
    deq.rotate(-k+1)
    answerlist.append(deq.popleft())

for i in range(len(answerlist)):
    if i == 0:
        print("<"+str(answerlist[i]),sep="",end="")
    
    else:
        print(", " + str(answerlist[i]),sep="",end="")

    if i == len(answerlist) - 1:
        print(">",sep="",end="")