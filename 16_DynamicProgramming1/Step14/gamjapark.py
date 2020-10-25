import sys
one = sys.stdin.readline().strip()
two = sys.stdin.readline().strip()

result = [[0] * (len(two)+1) for _ in range(len(one)+1)]

for i in range(1, len(one)+1):
    for j in range(1, len(two)+1):
        if one[i-1] == two[j-1]:
            result[i][j] = result[i-1][j-1] + 1
        else:
            result[i][j] = max(result[i][j-1], result[i-1][j])

print(result[len(one)][len(two)])