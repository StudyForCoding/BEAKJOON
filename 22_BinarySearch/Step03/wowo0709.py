import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LAN = []
for _ in range(K):
    LAN.append(int(input()))

low,high = 0, max(LAN)
tmp_n = 0
while low <= high:
    mid = (low + high) // 2
    if mid == 0:  break
    tmp_n = sum(map(lambda x:x//mid,LAN))
    if tmp_n >= N:  low = mid + 1
    else:  high = mid - 1