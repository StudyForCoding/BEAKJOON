import sys
input = sys.stdin.readline
k = int(input())
numlist = [0] # 합이 0일 때 고려
for i in range(k):
    num = int(input())
    if num == 0:
        numlist.pop()
    else:
        numlist.append(num)
print(sum(numlist))