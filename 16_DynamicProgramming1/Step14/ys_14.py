n = list(input()) # 행
m = list(input()) # 열

n_len = len(n)
m_len = len(m)

dp = [[0] * (m_len + 1) for i in range(n_len + 1)]
for i in range(n_len):
    for j in range(m_len):
        if n[i] == m[j]: #둘이 같으면
            dp[i + 1][j + 1] = dp[i][j] + 1 #dp에 +1
        else: #둘이 다르면
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) #이전 인덱스 최대값
print(dp[n_len][m_len])
