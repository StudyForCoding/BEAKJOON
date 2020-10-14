n = int(input())
stairnum = [[0 for j in range(10)] for i in range(n)]
stairnum[0][0:9] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    stairnum[i][0] = stairnum[i-1][1]
    stairnum[i][9] = stairnum[i-1][8]
    for j in range(1,9):
        stairnum[i][j] = stairnum[i-1][j-1] + stairnum[i-1][j+1]
print(sum(stairnum[n-1])%1000000000)