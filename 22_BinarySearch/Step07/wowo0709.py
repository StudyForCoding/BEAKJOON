'''
가장 긴 수열의 길이만을 구하면 된다는 것을 인지한다. 
배열(A) 안의 수들에 대해 각 수가 들어갈 위치(low<=,<high)를 구한다. 
1. 가장 긴 배열의 길이를 구하기 위한 리스트(ans), 최소 위치(low)=0, 최대 위치(high)=len(ans)-1,
   이분 탐색 인덱스 값(mid)=(low+high)//2 로 초기화
2. 해당 인덱스의 수가 삽입할 수보다 작거나 같다면 low=mid+1. 크다면 high=mid-1
3. 1~2 과정을 low <= high 인 동안 반복한다. 
4. 찾은 인덱스(low) 위치에 수를 삽입한다. 
'''
import sys
input = sys.stdin.readline
    
N = int(input())
A = list(map(int,input().split()))
ans = [0]

for i in range(N):
    low,high = 0,len(ans)-1
    while low <= high:
        mid = (low+high) // 2
        if ans[mid] < A[i]:
            low = mid+1
        else:
            high = mid-1
    if low >= len(ans):  ans.append(A[i])
    else:  ans[low] = A[i]
print(len(ans)-1)