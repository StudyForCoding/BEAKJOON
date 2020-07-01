N = int(input())
body = []
rank = {}
for i in range(N):
    rank[i] = 1
    body.append(list(map(int, input().split())))

for i in range(N - 1):
    for j in range(i + 1, N):
        if body[i][0] > body[j][0] and body[i][1] > body[j][1]:
            rank[j] += 1
        if body[j][0] > body[i][0] and body[j][1] > body[i][1]:
            rank[i] += 1
for i in range(N):
    print(rank[i], sep=' ')
