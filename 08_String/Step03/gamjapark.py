a = list(map(lambda i: ord(i) - 97, list(input())))
idx_array = [-1 for _ in range(26)]

for i in range(len(a)):
    if idx_array[a[i]] == -1:
        idx_array[a[i]] = i

for idx in idx_array:
    print(idx, end=' ')