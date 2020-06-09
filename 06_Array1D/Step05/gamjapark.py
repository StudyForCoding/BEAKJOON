import sys
n = int(input())
scores = list(map(int, sys.stdin.readline().rstrip().split()))
max_score = max(scores)
sum = 0
for i in range(n):
    sum += (scores[i] / max_score * 100)
print("%0.2f"%(sum/n))