import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split())) # 리스트 사용
M = int(input())
B = list(map(int,input().split()))

for b in B:
    answer = 1 if b in A else 0
    print(answer)