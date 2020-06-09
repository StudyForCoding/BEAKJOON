N=int(input())
count_list = []
for i in range(N//5 + 1):
    for j in range(N//3 + 1):
        if ((5 * i) + (3 * j)) == N:
            count_list.append(i + j)
print(min(count_list)) if len(count_list) > 0 else print(-1)
