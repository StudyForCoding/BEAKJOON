'''이분 탐색으로 구현하기'''
import sys
input = sys.stdin.readline

def BinarySearch(low,high,target):
    if low > high:  return 0

    mid = (low+high)//2
    if A[mid] == target:  return 1
    elif A[mid] > target:  return BinarySearch(low,mid-1,target)
    else:  return BinarySearch(mid+1,high,target)


N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = list(map(int,input().split()))
for b in B:
    print(BinarySearch(0,N-1,b))