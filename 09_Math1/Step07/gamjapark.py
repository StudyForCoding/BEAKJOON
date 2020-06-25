T = int(input())
for i in range(T):
    a = int(input())
    b = int(input())
    save = [[0 for _ in range(b)] for _ in range(a + 1)]
    for i in range(b):
        save[0][i] = i + 1
    for i in range(1, a + 1):
        save[i][0] = 1
    for i in range(1, a + 1):
        for j in range(1, b):
            save[i][j] = save[i - 1][j] + save[i][j - 1]
    print(save[a][b - 1])