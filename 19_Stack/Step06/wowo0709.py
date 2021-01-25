import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
# Oks에는 오큰수, s에는 아직 오큰수를 찾지 못한 인덱스를 저장
Oks,s = [-1 for _ in range(n)],[]

for i in range(n):
    # 스택이 비지 않았고 오큰수를 찾지 못한 수들 중 가장 오른쪽 
    # 수가 현재 수보다 작다면,
    while s and nums[s[-1]] < nums[i]:
        # 해당 수의 오큰수는 현재 수가 됨.
        Oks[s.pop()] = nums[i]
    s.append(i)
    
print(*Oks)