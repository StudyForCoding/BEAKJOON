import sys
input = sys.stdin.readline

n = int(input())
seq = []  # 주어진 수열
stack = []  # 1부터 n까지 오름차순으로 push될 스택
op = [] # operator 출력용 
for _ in range(n):
    seq.append(int(input()))
seq.reverse()
for i in range(1,n+1):
    stack.append(i)
    op.append('+')
    while stack:
        if stack[-1] == seq[-1]:
            stack.pop()
            seq.pop()
            op.append('-')
        else:
            break
if stack: # 실패 시 스택이 비어있지 않음
    print('NO')
else: # 성공 시 스택이 비어있음
    for i in op:
        print(i)