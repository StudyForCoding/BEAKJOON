import sys
input = sys.stdin.readline

def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]
    num[start][0].append(start)
    for i in tree[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)
            if max(dp[i][1], dp[i][0]) == dp[i][1]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)

# main
n = int(input())
w = [0] + list(map(int, input().split()))
tree = [[] for i in range(n + 1)]
dp = [[0,0] for i in range(n + 1)] # 가중치 합, 본인 포함 여부(0:포함,1:미포함)
visit = [False for i in range(n + 1)]
num = [[[], []] for i in range(n + 1)] # 본인 포함, 본인 미포함 시의 노드 집합
for i in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
if max(dp[1][0], dp[1][1]) == dp[1][0]:
    ans1 = dp[1][0]
    ans2 = num[1][0]
else:
    ans1 = dp[1][1]
    ans2 = num[1][1]
print(ans1)
print(*sorted(ans2))

