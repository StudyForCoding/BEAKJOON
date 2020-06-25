N = int(input())
arr = [[' ' for _ in range(N)] for _ in range(N)]

def star(n, x, y):
    if n == 1:
        arr[x][y] = "*"
    else:
        val = n // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    star(val, x + (val * i), y + (val * j))

star(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(arr[i][j], end="")
    print()