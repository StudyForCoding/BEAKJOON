'''
***in연산자의 시간 복잡도***
: 리스트의 경우 O(n), 딕셔너리와 집합의 경우 평균적으로 O(1), 최악의 경우에 O(n)
실제로 이 문제의 경우 리스트로 풀이 시 3700ms, 집합으로 풀이 시 224ms가 걸림.
'''
import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int,input().split())) # 셋 사용
M = int(input())
B = list(map(int,input().split()))

for b in B:
    answer = 1 if b in A else 0
    print(answer)